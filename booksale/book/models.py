from django.db import models

# Create your models here.
class User(models.Model):

    class Meta:
        verbose_name_plural = verbose_name = "用户表"

    name = models.CharField(default='', max_length=100, verbose_name='姓名')
    username = models.CharField(default='',max_length=100, verbose_name='用户名')
    password = models.CharField(default='',max_length=100, verbose_name='密码')
    address = models.CharField(default='',max_length=500, verbose_name='地址')
    phone = models.CharField(default='',max_length=200, verbose_name='电话号码')
    money = models.IntegerField(default=0, verbose_name='金额')

    def __str__(self):
        return self.name

