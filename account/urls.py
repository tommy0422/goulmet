from django.urls import path
from .views import UserUpdate,UserDetail,logout,PasswordChange,PasswordChangeDone

app_name = "account"

urlpatterns = [
    path('user_update/<int:pk>', UserUpdate.as_view(), name='user_update'),
    path('user_detail/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('pass_change/', PasswordChange.as_view(), name='pass_change'),
    path('pass_change/done/', PasswordChangeDone.as_view(), name='pass_change_done'),
    path('logout/', logout, name='logout'),
]