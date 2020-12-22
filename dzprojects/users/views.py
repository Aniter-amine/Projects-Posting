from django.shortcuts import render, redirect, get_object_or_404
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm, ProfForm
from .models import Prof


class ProfilePage(DetailView):
    model = User
    template_name = 'auths/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


@login_required(login_url='login')
def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request, 'auths/logout.html')


@unauthenticated_user
def register_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='member')
            user.groups.add(group)
            messages.success(
                request, f'The Account Was Successfully For { username }')
            return redirect('login')

    context = {"form": form}
    return render(request, 'auths/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(
                request, f'Successfully Logged In Mr.{ username }')
            return redirect('index')
        else:
            messages.info(request, f'Username Or Password Incorrect')
    context = {}
    return render(request, 'auths/login.html', context)


def MyProfile(request):
    user = request.user.prof
    form = ProfForm(instance=user)
    if request.method == "POST":
        form = ProfForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'auths/myprofile.html', context)
