from django.urls import path

from .views import RegisterView, LoginUserView, LogoutUserView, ProfileUserDetailView, ProfileUserUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutUserView.as_view(next_page='med_center:home'), name='logout'),

    path('profile/<int:pk>/', ProfileUserDetailView.as_view(), name='profile_user'),
]
