from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .services import UserIsNotAuthenticated

User = get_user_model()


class ProfileUserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile_user.html"
    context_object_name = "profile_user"


# class ProfileUserUpdateView(LoginRequiredMixin, UpdateView):
#     model = User
#     template_name = 'users/register.html'
#     form_class = ProfileForm
#
#     context_object_name = "profile_edit"
#
#     def get_success_url(self):
#         return reverse("users:profile_user", args=[self.kwargs.get("pk")])


# class LoginUserView(LoginView):
#     form_class = LoginUserForm
#
#
# class LogoutUserView(LoginRequiredMixin, LogoutView):
#     success_url = reverse_lazy('med_center:home')


class RegisterView(UserIsNotAuthenticated, CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("med_center:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация на сайте"
        return context
