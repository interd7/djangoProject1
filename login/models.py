from django.db import models

# Create your models here.
from django.db import models


class RegisterUser(models.Model):
    reg_mail=models.CharField(max_length=100,blank=False)#邮箱
    reg_pwd=models.CharField(max_length=100,blank=False)#密码
