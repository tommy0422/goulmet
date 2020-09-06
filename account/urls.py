from django.urls import path
from .views import UserUpdate,logout,PasswordChange,PasswordChangeDone

app_name = "account"

urlpatterns = [
    path('user_update/<int:pk>', UserUpdate.as_view(), name='user_update'),
    path('pass_change/', PasswordChange.as_view(), name='pass_change'),
    path('pass_change/done/', PasswordChangeDone.as_view(), name='pass_change_done'),
    path('logout/', logout, name='logout'),
]