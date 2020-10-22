from django.urls import path
from .views import user_update,user_detail,logout,PasswordChange,PasswordChangeDone,goulmet_create,judge_start,additional_option,goulmet_update, goulmet_detail,option_list,OptionDelete,OptionUpdate

app_name = "account"

urlpatterns = [
    path('user_update/', user_update, name='user_update'),
    path('user_detail/', user_detail, name='user_detail'),
    path('pass_change/', PasswordChange.as_view(), name='pass_change'),
    path('pass_change/done/', PasswordChangeDone.as_view(), name='pass_change_done'),
    path('logout/', logout, name='logout'),
    path('goulmet_create/',goulmet_create,name='goulmet_create'),
    path('judge_start/',judge_start,name='judge_start'),
    path('additional_option/',additional_option,name='additional_option'),
    path('goulmet_update/',goulmet_update,name='goulmet_update'),
    path('goulmet_detail/',goulmet_detail,name='goulmet_detail'),
    path('option_list/',option_list,name='option_list'),
    path('option_delete/<int:pk>',OptionDelete.as_view(),name='option_delete'),
    path('option_update/<int:pk>',OptionUpdate.as_view(),name='option_update'),
]