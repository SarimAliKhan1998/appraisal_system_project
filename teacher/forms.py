from django import forms
from .models import Teacher
from user.models import User
from department.models import Department


class TeacherModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request')
        super(TeacherModelForm, self).__init__(*args, **kwargs)

        self.fields['department'] = forms.ModelChoiceField(
            queryset= Department.objects.all()
        )


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
