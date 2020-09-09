from django.urls import path
from .views import RegisterView,loginfunc ,TopView

app_name = "register"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', loginfunc, name='login'),
    path('top/', TopView.as_view(), name='top'),
]