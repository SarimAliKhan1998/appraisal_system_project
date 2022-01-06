from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    hod = models.OneToOneField('teacher.Teacher', null= True, blank= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.department_name