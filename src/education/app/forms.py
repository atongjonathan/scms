from django.core.files.uploadedfile import UploadedFile
from os.path import join
from django.conf import settings
from constance import config
from datetime import datetime
from django.utils import timezone
from authentication.storages_backends import R2UserImageStorage
from constance.forms import ConstanceForm as BaseConstanceForm
from django.utils.text import normalize_newlines
from django import conf


class R2ConstanceForm(BaseConstanceForm):
    def save(self):
        r2_storage = R2UserImageStorage()

        for file_field in self.files:
            file = self.cleaned_data[file_field]
            if isinstance(file, UploadedFile):
                # Always save to R2 storage
                self.cleaned_data[file_field] = r2_storage.save(
                    join(file_field, file.name), file
                )

        for name in settings.CONFIG:
            current = getattr(config, name)
            new = self.cleaned_data[name]

            if isinstance(new, str):
                new = normalize_newlines(new)

            if conf.settings.USE_TZ and isinstance(current, datetime) and not timezone.is_aware(current):
                current = timezone.make_aware(current)

            if current != new:
                setattr(config, name, new)
