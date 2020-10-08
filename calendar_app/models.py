import datetime
from django.db import models
from django.utils import timezone
from account.models import GoulmetModel

# Create your models here.
class Schedule(models.Model):
    """スケジュール"""
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    user_id = models.ForeignKey(GoulmetModel,db_column='user_id',on_delete=models.CASCADE )

    def __str__(self):
        return str(self.date) + ' ' + str(self.start_time) + ' ' + str(self.user_id)