from django import forms
from .storages_backends import R2UserImageStorage


class R2ImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("required", False)
        super().__init__(*args, **kwargs)
        self.storage = R2UserImageStorage()
