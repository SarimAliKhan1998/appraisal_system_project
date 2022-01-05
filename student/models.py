from django.db import models

# from user.models import User

class Student(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    roll_no = models.BigIntegerField(blank= True, null= True)
    date_of_birth = models.DateField(blank= True, null=True)
    department = models.ForeignKey('department.Department', null=True, blank= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user + " " + self.department