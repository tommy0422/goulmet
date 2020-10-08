from django.db import models
import datetime
from myuser.models import CustomUser
from account.models import GoulmetModel,OptionModel

# Create your models here.
class OrderModel(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user_id')
    goulmet_id = models.ForeignKey(GoulmetModel,on_delete=models.CASCADE,related_name='goulmet_id')
    base_price = models.IntegerField('基本料金')
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))

    def __str__(self):
        return str(self.user_id) + '&' + str(self.goulmet_id)

class OrderOption(models.Model):
    order_id = models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    option_id = models.ForeignKey(OptionModel,on_delete=models.CASCADE)
    option_price = models.IntegerField('追加料金')

    def __str__(self):
        return str(self.user_id) + ' ' + str(self.option_id)