from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'register/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register:login')

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #認証成功するかしないか
        if user is not None:
            login(request, user)
            return redirect('register:top')
        else:
            return redirect('register:login')
    return render(request, 'register/login.html')

class TopView(TemplateView):
    template_name = 'register/top.html'