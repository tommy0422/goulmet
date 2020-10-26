from django.urls import path
from .views import chat_list, chat_list_goulmet, user_chat,userchat_create,goulmet_chat,goulmetchat_create

app_name = 'chat'

urlpatterns = [
    path('chat_list/',chat_list,name='chat_list'),
    path('chat_list_goulmet/',chat_list_goulmet,name='chat_list_goulmet'),
    path('user_chat/<int:pk>', user_chat, name='user_chat'),
    path('userchat_create/',userchat_create,name='userchat_create'),
    path('goulmet_chat/<int:pk>', goulmet_chat, name='goulmet_chat'),
    path('goulmetchat_create/',goulmetchat_create,name='goulmetchat_create'),
]