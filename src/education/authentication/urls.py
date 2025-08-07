from django.urls import path
from . import views

urlpatterns = [
    path("login", views.Login.as_view(), name="login"),
    path("logout", views.Logout.as_view(), name="logout"),
    # URL for password reset request
    path('password-reset/', views.PasswordReset.as_view(), name="password_reset",),
    path('password-reset/done/', views.PasswordResetDone.as_view(),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.PasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path('password-reset-complete/',
         views.PasswordResetComplete.as_view(), name="password_reset_complete"),


]
