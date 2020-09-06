from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from .forms import UserUpdateForm, MyPasswordChangeForm
from myuser.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


# Create your views here.
class UserUpdate(UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'account/user_info.html'

@login_required
def logout(request):
    django_logout(request)
    return redirect('register:login')

class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('account:pass_change_done')
    template_name = 'account/pass_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'account/pass_change_done.html'





