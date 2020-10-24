from django.urls import path
from .views import chat_list, chat_list_goulmet, user_chat

app_name = 'chat'

urlpatterns = [
    path('chat_list/',chat_list,name='chat_list'),
    path('chat_list_goulmet/',chat_list_goulmet,name='chat_list_goulmet'),
    path('user_chat/', user_chat, name='user_chat'),
]