from django.db import models

# Create your models here.
class User(models.Model):

    class Meta:
        verbose_name_plural = verbose_name = "用户表"

    name = models.CharField(max_length=100, verbose_name='姓名')
    username = models.CharField(max_length=100, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')

    def __str__(self):
        return self.name