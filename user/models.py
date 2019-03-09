from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    qq = models.CharField('QQ号码',max_length=20)
    weChat = models.CharField('微信',max_length=20)
    mobile = models.CharField('手机号码',max_length=11,unique=True)

    def __str__(self):
        return self.username;