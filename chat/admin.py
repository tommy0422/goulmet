from django.contrib import admin
from chat.models import RoomModel, ChatModel

# Register your models here.
admin.site.register(RoomModel)
admin.site.register(ChatModel)