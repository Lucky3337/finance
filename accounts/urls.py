from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views


from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),

    # todo need to fix the bug with reset password by email
    # Password Reset Url's
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('password_reset_done')
    ), name="password_reset"),
    path('accounts/password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_change_done.html'
    ), name="password_reset_done"),
]