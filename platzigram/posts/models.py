#Post models.

#Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        #Return title an dusername
        return f'{self.title} by @{self.user.username}'