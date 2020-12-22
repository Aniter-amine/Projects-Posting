from django.urls import path, include
from .views import ProfilePage
from . import views
urlpatterns = [
    path('logout/',
         views.logout_page, name="logout"),
    path('login/', views.login_page, name="login"),
    path('profile/<int:pk>', ProfilePage.as_view(), name="profile"),
    path('myprofile/', views.MyProfile, name="myprofile"),
    path('register/', views.register_page, name="register"),
]
