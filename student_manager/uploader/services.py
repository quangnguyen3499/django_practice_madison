from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
from .models import Upload

class PublicS3MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    default_acl = 'public-read'
    location = 'media'

def file_upload(file):
    upload = Upload(file=file)
    upload.save()
    return upload.image_url
