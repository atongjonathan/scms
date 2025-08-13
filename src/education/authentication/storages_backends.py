from storages.backends.s3boto3 import S3Boto3Storage
import os


class R2UserImageStorage(S3Boto3Storage):
    bucket_name = os.getenv("R2_BUCKET_NAME")
    account_id = os.getenv("R2_ACCOUNT_ID")
    endpoint_url = f"https://{account_id}.r2.cloudflarestorage.com"
    default_acl = "public-read"
    file_overwrite = False
