from django.db import models

# from user.models import User

class Student(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)