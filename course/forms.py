from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


from .models import CourseClass
from student.models import Student

class CourseClassModelForm(forms.ModelForm):
    # in this form, once the course name is selected, let the teachers field only display the teachers that belong to the 
    # department that the course has been attributed to

    class Meta:
        model = CourseClass
        fields = "__all__"
    
    
    def __init__(self, *args, **kwargs):
        super(CourseClassModelForm, self).__init__(*args, **kwargs)

        self.fields['students'].widget = CheckboxSelectMultiple()
        self.fields['students'].queryset = Student.objects.all()      # just adding this for now, so that we can manipulate later if needed