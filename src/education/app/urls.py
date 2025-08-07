from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path('password-change',
         views.PasswordChange.as_view(), name="password_change"),
    path('password-change/done',
         views.PasswordChangeDone.as_view(), name="password_change_done"),
    path('profile/<str:email>',
         views.Profile.as_view(), name="profile"),
    path('profile/<str:email>/edit',
         views.UpdateProfile.as_view(), name="profile_edit"),

]
