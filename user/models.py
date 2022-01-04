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
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null = True, blank= True)
    year_of_joining = models.IntegerField(null=True, blank=True)
    is_admin = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.username + f"\tAdmin : {self.is_admin} \tTeacher : {self.is_teacher} \tStudent : {self.is_student}"
