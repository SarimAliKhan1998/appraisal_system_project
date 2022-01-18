from django.db import models

class Course(models.Model):

    course_code = models.CharField(max_length=12, blank = True, null = True)
    course_name = models.CharField(max_length=70)
    department = models.ForeignKey('department.Department', on_delete = models.CASCADE)
    for_semester = models.IntegerField(blank= True, null= True)

    def __str__(self):
        return  f"{self.course_name} - {self.department.department_name} Department"


class CourseClass(models.Model):

    course = models.ForeignKey('course.Course', blank= True, null= True, on_delete= models.SET_NULL)
    teacher = models.ForeignKey('teacher.Teacher', blank= True, null= True, on_delete=models.SET_NULL)
    # section = models.CharField(max_length=1, blank=True, null= True)
    batch_name = models.CharField(max_length=20, blank=True, null= True)             # something like 'into to ds - 7th sem -section a'
    students = models.ManyToManyField('student.Student', blank= True, null= True)

    def __str__(self):
        return f"{self.course} - {self.teacher}"
        return f"{self.batch_name}"
        # return f"{self.course} - Section {self.section} - {self.teacher}"


class Attendance(models.Model):

    date = models.DateTimeField()
    subject = models.OneToOneField('course.CourseClass', blank= True, null= True, on_delete= models.SET_NULL)
    student = models.OneToOneField('student.Student', blank= True, null= True, on_delete= models.SET_NULL) 
    no_of_attendances_possible = models.IntegerField(blank=True, null=True, default=1) 
    no_of_attendances_granted = models.IntegerField(blank=True, null=True, default=1) 
    # when creating the view for adding attendance, we need to check that only the students who are in a particular
    # course are selected for the attendance  


    # also, add semester and section fields to student model if needed


class Ratings(models.Model):

    student = models.ForeignKey('student.Student', blank= True, null= True, on_delete= models.SET_NULL)
    teacher = models.ForeignKey('teacher.Teacher', blank= True, null= True, on_delete= models.SET_NULL)