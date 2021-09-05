from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext
# Create your models here.


class Profile(models.Model):
    bio = models.TextField(default=gettext('no bio ...'))
    picture = models.ImageField(
        upload_to='user_picture', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=30, choices=settings.LANGUAGES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.username}"
