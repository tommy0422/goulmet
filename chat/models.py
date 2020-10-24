from django.db import models
from myuser.models import CustomUser
from account.models import GoulmetModel
from calendar_app.models import Schedule
from reservation.models import OrderModel


# Create your models here.
class RoomModel(models.Model):
    """チャットルーム"""
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    goulmet_id = models.ForeignKey(GoulmetModel,on_delete=models.CASCADE)
    order_id = models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時',auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)

    def __str__(self):
        return str(self.user_id.username) + '&' + str(self.goulmet_id.user_id) + ' ' + str(self.order_id.date)

class ChatModel(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    goulmet_id = models.ForeignKey(GoulmetModel,on_delete=models.CASCADE,null=True)
    room_id = models.ForeignKey(RoomModel,on_delete=models.CASCADE)
    text = models.IntegerField('メッセージ')
    created_at = models.DateTimeField('作成日時',auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)
    
    def __str__(self):
        if user_id:
            return str(self.user_id) + ' ' + str(self.created_at)
        else:
            return str(self.goulmet_id) + ' ' + str(self.created_at)