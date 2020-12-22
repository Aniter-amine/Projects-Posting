from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from .forms import ProjectForm, EditForm
from django.urls import reverse
from .models import Project
from users.models import Prof
import requests


# Index View
def index(request):
    return render(request, 'index.html')


def rules(request):
    return render(request, 'rules.html')


class ProjectsView(ListView):
    model = Project
    template_name = 'project.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_details.html'

    def get_object(self):
        obj = super().get_object()
        obj.project_views += 1
        obj.save()
        return obj


class AddProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'add_project.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.username
        form.instance.author_id = self.request.user.id
        form.instance.author_avatar = self.request.user.prof.image.url
        return super().form_valid(form)


class UpdateProjectView(UpdateView):
    model = Project
    template_name = 'update_project.html'
    form_class = EditForm


class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'delete_project.html'
    success_url = reverse_lazy('project')
