from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    bio = models.TextField(default='no bio ...')
    picture = models.ImageField(
        upload_to='user_picture', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.username}"
