from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from myuser.models import CustomUser
from django.contrib.auth import get_user_model

class UserUpdateForm(ModelForm):
    """"ユーザー情報更新フォーム"""
    class Meta:
        model = CustomUser
        fields = ('icon','username','email')

class MyPasswordChangeForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'