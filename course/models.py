from django.db import models

class Course(models.Model):

    course_name = models.CharField(max_length=70)
    department = models.ForeignKey('department.Department', on_delete = models.CASCADE)
    for_semester = models.IntegerField(blank= True, null= True)

    def __str__(self):
        return self.name + f" - {self.department.department_name} Department"



class CourseClass(models.Model):

    course = models.ForeignKey('course.Course', blank= True, null= True, on_delete= models.SET_NULL)
    teacher = models.ManyToManyField('teacher.Teacher', blank= True, null= True)
    section = models.CharField(max_length=1, blank=True, null= True)
    students = models.ManyToManyField('student.Student', blank= True, null= True)

    def __str__(self):
        return self.course + f" - Section {self.section} - {self.teacher}"


class Attendance(models.Model):

    date = models.DateTimeField()
    subject = models.OneToOneField('course.CourseClass', blank= True, null= True, on_delete= models.SET_NULL)
    student = models.OneToOneField('student.Student', blank= True, null= True, on_delete= models.SET_NULL)  
    # when creating the view for adding attendance, we need to check that only the students who are in a particular
    # course are selected for the attendance  


    # also, add semester and section fields to student model if needed


class Ratings(models.Model):

    student = models.ForeignKey('student.Student', blank= True, null= True, on_delete= models.SET_NULL)
    teacher = models.ForeignKey('teacher.Teacher', blank= True, null= True, on_delete= models.SET_NULL)