from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django_registration.backends.activation import views as registration_views
from django_registration.backends.activation.urls import urlpatterns
urlpatterns


app_name = 'accounts'

urlpatterns = [
    # Registration.
    path('accounts/activate/complete/', registration_views.RegistrationView.as_view(
        template_name='django_registration/activation_complete.html'),
         name='django_registration_activation_complete'),
    url(r'^accounts/activate/(?P<activation_key>[-:\w]+)/$',
        registration_views.ActivationView.as_view(
            success_url=reverse_lazy('accounts:django_registration_activation_complete')
        ), name='django_registration_activate'),
    path('accounts/register/', registration_views.RegistrationView.as_view(
        success_url=reverse_lazy('accounts:django_registration_complete'),
    ), name='django_registration_register'),
    path('accounts/register/complete', registration_views.RegistrationView.as_view(
        template_name='django_registration/registration_complete.html',
        success_url=reverse_lazy('accounts:django_registration_complete'),
    ), name='django_registration_complete'),
    path('accounts/register/closed/', registration_views.RegistrationView.as_view(),
         name='django_registration_disallowed'),


    # Authentication
    path('accounts/login/', auth_views.LoginView.as_view(),
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/password_change/done', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        success_url=reverse_lazy('accounts:password_reset_done')
    ), name="password_reset"),
    path('accounts/password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name="password_reset_done"),
    path('accounts/reset/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete')
    ),name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]