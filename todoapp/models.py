from django.db import models

from django.contrib.auth.models import User, auth

# Create your models here.

class todo(models.Model):
    author = models.ForeignKey(User,  to_field='username',default='root', on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text