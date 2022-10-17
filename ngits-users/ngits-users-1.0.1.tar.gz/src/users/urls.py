from django.urls import path

from . import views

urlpatterns = [
    path(
        "background_registration/",
        views.BackgroundRegistrationView.as_view(),
        name="background_registration",
    ),
    path(
        "registration/",
        views.StandardRegistrationView.as_view(),
        name="registration",
    ),
    path("login/", views.StandardLoginView.as_view(), name="login"),
    path(
        "change_password/",
        views.ChangePasswordView.as_view(),
        name="change_password",
    ),
    path(
        "remind_password/",
        views.RemindPasswordView.as_view(),
        name="remind_password",
    ),
    path(
        "delete_account/",
        views.DeleteAccountView.as_view(),
        name="delete_account",
    ),
    path(
        "google_auth/",
        views.GoogleAuthorizationView.as_view(),
        name="google_auth",
    ),
    path(
        "facebook_auth/",
        views.FacebookAuthorizationView.as_view(),
        name="facebook_auth",
    ),
    path("verify/", views.VerifyAccountView.as_view(), name="verify"),
    path(
        "confirm_remind_password/",
        views.RemindPasswordConfirmView.as_view(),
        name="remind_password_confirm",
    ),
]
