from django.db import models

from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    ADMIN = 1
    TEACHER = 2
    STUDENT = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key= True)

    def __str__(self):
        return self.id



class User(AbstractUser):
    pass
    # role = models.ManyToManyField(Role)
    is_admin = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.username + f"\tAdmin : {self.is_admin} \tTeacher : {self.is_teacher} \tStudent : {self.is_student}"
