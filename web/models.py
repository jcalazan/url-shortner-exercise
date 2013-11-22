import hashlib
import base64

from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base class that provides self-updating 'created' and 'modified'
    fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ShortenedUrlManager(models.Manager):

    def original_exists(self, url):
        exists = False
        if self.filter(original=url):
            exists = True

        return exists

    def already_shortened(self, url):
        is_shortened = False
        if self.filter(shortened=url):
            is_shortened = True

        return is_shortened

    def shorten(self, original_url):
        """
        Generates a value to use for the shortened URL that is URL-safe.

        Steps:
            1. Generate an MD5 checksum of the given URL to produce a
            random/unique string/digest.
            2. Base64-encode the MD5 checksum to create a URL-safe value.
            3. Strip the '=' sign as it will get in the way of capturing URL
            parameters.
            4. Take the first 5 characters from the encoded value.

        Caveats:
            1. Collision is possible since we're only taking the first 5
            characters, but it would still take a very large number of records
            before this becomes an issue.
        """
        checksum = hashlib.md5(original_url).digest()
        value = base64.urlsafe_b64encode(checksum).strip('=')

        return value[:5]


class ShortenedUrl(TimeStampedModel):
    """
    Store the original URL provided by the user and the shortened version
    generated by the system.
    """
    objects = ShortenedUrlManager()

    original = models.URLField(
        unique=True, null=False, blank=False, max_length=5000)
    shortened = models.CharField(
        unique=True, null=False, blank=False, max_length=5000)
