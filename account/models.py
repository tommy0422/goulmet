from django.db import models
from myuser.models import CustomUser

# Create your models here.
class OptionModel(models.Model):
    option = models.CharField('オプション内容',max_length=100)
    price = models.IntegerField('追加料金')
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.option + ' ' + str(self.user_id)

class GoulmetModel(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    self_introduction = models.TextField('自己紹介',max_length=140)
    area = models.CharField('地域',max_length=50)
    plan = models.TextField('プラン',max_length=50,null=True)
    base_price = models.IntegerField('基本料金')
    is_pass = models.BooleanField('審査合格フラグ',null=True)
    created_at = models.DateTimeField('作成日時',auto_now_add=True)

    def __str__(self):
        return str(self.user_id)