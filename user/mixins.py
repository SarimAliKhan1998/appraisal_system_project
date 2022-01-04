from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin


class LoginAndAdminMixin(AccessMixin):
    '''
    Verify that the current user is logged in and is an admin
    '''

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin :
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)


class LoginAndAdminAndTeacherMixin(AccessMixin):
    '''
    Verify that the current user is logged in and is either an admin or a teacher
    '''

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin or not request.user.is_teacher :
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)