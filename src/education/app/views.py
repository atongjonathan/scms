from math import perm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views

# Create your views here.


@method_decorator(login_required, name="dispatch")
class Index(TemplateView):
    template_name = "app/layout.html"
    extra_context = {"title": "Home"}


class PasswordChange(auth_views.PasswordChangeView):
    template_name = "authentication/password_change_form.html"
    extra_context = {"title": "Password change"}


class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name = "authentication/password_change_done.html"
    extra_context = {"title": "Password change successful"}
