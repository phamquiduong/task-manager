from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=255)

    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    avatar_key = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = 'users'

    def save(self, *args, **kwargs) -> None:
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)


class UserTemp(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    expired_datetime = models.DateTimeField()

    class Meta:
        db_table = 'user_temps'


class EmailOtp(models.Model):
    user_email = models.ForeignKey(User, to_field='email', on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    expired_datetime = models.DateTimeField()

    class Meta:
        db_table = 'email_otps'


class UserSession(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=255)
    expired_datetime = models.DateTimeField()

    class Meta:
        db_table = 'user_sessions'
