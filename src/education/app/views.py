from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.models import EUser
from django.core.exceptions import PermissionDenied


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


class Profile(LoginRequiredMixin, DetailView):
    model = EUser
    template_name = "authentication/profile.html"
    slug_field = "email"
    slug_url_kwarg = "email"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj != self.request.user:
            raise PermissionDenied("You cannot view another user's profile.")
        return obj

    def get_context_data(self, **kwargs):
        kwargs.update({
            "title": f"Profile - {self.request.user.full_name}",
        })
        return super().get_context_data(**kwargs)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = EUser
    fields = ['first_name', 'middle_name',
              'last_name', 'user_image', 'mobile_number']
    template_name = "authentication/profile_edit.html"
    slug_field = "email"
    slug_url_kwarg = "email"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj != self.request.user:
            raise PermissionDenied("You cannot edit another user's profile.")
        return obj

    def get_context_data(self, **kwargs):
        kwargs.update(
            {"title": f'Update Profile - {self.request.user.full_name}'})
        return super().get_context_data(**kwargs)

    def form_invalid(self, form):
        print(form.error_class)
        return super().form_invalid(form)

    def form_valid(self, form):
        if self.request.POST.get('clear_user_image'):
            form.instance.user_image.delete(save=False)
            form.instance.user_image = None

        return super().form_valid(form)
