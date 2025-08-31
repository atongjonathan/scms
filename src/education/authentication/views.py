from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class Login(auth_views.LoginView):
    template_name = "authentication/login.html"
    redirect_authenticated_user = True
    extra_context = {"title": "Login to ScMS"}

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
    title = "Password change"


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = "authentication/password_reset_confirm.html"


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = "authentication/password_reset_done.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = "authentication/password_reset_complete.html"


class PasswordChange(auth_views.PasswordChangeView):
    template_name = "authentication/password_change_form.html"


class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name = "authentication/password_change_done.html"
    
    def get(self, request, *args, **kwargs):
        messages.success(request, _("Your password was changed successfully!"))
        return HttpResponseRedirect(reverse_lazy('index'))
