from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .apps import UsersConfig
from .views import RegisterView, ProfileUserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="med_center:home"), name="logout"),
    path("profile/<int:pk>/", ProfileUserDetailView.as_view(), name="profile_user"),
]
