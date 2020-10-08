from django.urls import path
from .views import RegisterView,loginfunc

app_name = "register"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', loginfunc, name='login'),
]