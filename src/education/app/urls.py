from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path('settings', views.ConstanceView.as_view(), name='settings'),
    path('profile/<str:email>',
         views.UpdateProfile.as_view(), name="profile_edit"),
]
