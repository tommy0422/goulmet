from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from myuser.models import CustomUser
from .models import GoulmetModel, OptionModel
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

 # フォームに、取得したDayModelを紐付ける
class GoulmetUpdateForm(ModelForm):
    """"Goulmet情報更新フォーム"""
    class Meta:
        model = GoulmetModel
        fields = ('user_id','self_introduction','area','plan','base_price')

class OptionUpdateForm(ModelForm):
    """追加オプション編集フォーム"""
    class Meta:
        model = OptionModel
        fields = ('option','price')