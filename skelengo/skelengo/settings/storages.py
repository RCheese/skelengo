from storages.backends.s3boto3 import S3Boto3Storage

from .location import CONTENT_LOCATION, MEDIA_LOCATION, PRIVATE_MEDIA_LOCATION, STATIC_LOCATION, WEB_CONTENT_LOCATION


class StaticStorage(S3Boto3Storage):
    location = STATIC_LOCATION
    default_acl = "public-read"
    file_overwrite = True


class PublicMediaStorage(S3Boto3Storage):
    location = MEDIA_LOCATION
    default_acl = "public-read"
    file_overwrite = True


class MediaStorage(S3Boto3Storage):
    location = MEDIA_LOCATION
    default_acl = "public-read"
    file_overwrite = True


class PrivateMediaStorage(S3Boto3Storage):
    location = PRIVATE_MEDIA_LOCATION
    default_acl = "private"
    file_overwrite = True
    custom_domain = False
    querystring_expire = 600


class ContentStorage(S3Boto3Storage):
    default_content_type = "text/html"
    location = CONTENT_LOCATION
    default_acl = "public-read"
    file_overwrite = True


class WebContentStorage(S3Boto3Storage):
    default_content_type = "text/html"
    location = WEB_CONTENT_LOCATION
    default_acl = "public-read"
    file_overwrite = True
