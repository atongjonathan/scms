from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views


class Login(auth_views.LoginView):
    template_name = "authentication/login.html"
    redirect_authenticated_user = True
    extra_context = {"heading": "Login to SCMS"}

    def form_valid(self, form):
        # Validate if the username (email) exists
        email = form.data.get('email')
        username = email  # In case email is the same as username
        password = form.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid credentials")
            return self.form_invalid(form)


class Logout(auth_views.LogoutView):
    template_name = "authentication/logged_out.html"


class PasswordReset(auth_views.PasswordResetView):
    template_name = "authentication/password_reset_form.html"
    extra_context = {"heading": "Password Reset"}
    title = "Password change"


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = "authentication/password_reset_confirm.html"
    extra_context = {"heading": "Enter new password"}


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = "authentication/password_reset_done.html"
    extra_context = {"heading": "Password Reset"}

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = "authentication/password_reset_complete.html"
    extra_context = {"heading": "Password reset complete"}


class PasswordChange(auth_views.PasswordChangeView):
    template_name = "authentication/password_change_form.html"
    extra_context = {"heading": "Password change"}


class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name = "authentication/password_change_done.html"
    extra_context = {"heading": "Password change done"}
