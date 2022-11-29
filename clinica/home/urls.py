from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy

from home import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("about_me/", views.about_me, name="about_me"),
    path("search/", views.search, name="search"),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path("signup/", views.signup, name="user-signup"),
    path('register/profile/', views.user_profile, name='user-profile'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url=reverse_lazy("home:password-change-done")
        ),
        name="password-change"
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/change-password-done.html'
        ),
        name="password-change-done"
    ),
]
