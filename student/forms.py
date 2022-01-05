from django import forms
from .models import Student
from user.models import User
from department.models import Department


class StudentModelForm(forms.ModelForm):
    # roll_no = forms.IntegerField()


    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request')
        super(StudentModelForm, self).__init__(*args, **kwargs)

        self.fields['department'] = forms.ModelChoiceField(
            queryset= Department.objects.all()
        )
        self.fields['date_of_birth'] = forms.DateField()


    class Meta:
        model = User

        fields = (
            'first_name',
            'last_name',
            # 'username',
            "email",
            'phone_no',
            'address',
            'year_of_joining',

        )

    # select specific fields based on students