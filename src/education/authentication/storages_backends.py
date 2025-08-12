from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class R2UserImageStorage(S3Boto3Storage):
    bucket_name = settings.R2_BUCKET_NAME
    endpoint_url = f"https://{settings.R2_ACCOUNT_ID}.r2.cloudflarestorage.com"
    default_acl = "public-read"
