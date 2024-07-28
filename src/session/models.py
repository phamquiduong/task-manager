from django.db import models


class Session(models.Model):
    user_id = models.BigIntegerField()
    user_agent = models.CharField(max_length=255)
    expired_datetime = models.DateTimeField()

    class Meta:
        db_table = 'sessions'
