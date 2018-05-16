from django.db import models

# Create your models here.
class User(models.Model):

    class Meta:
        verbose_name_plural = verbose_name = "用户"

    name = models.CharField(default='', max_length=100, verbose_name='姓名')
    username = models.CharField(default='',max_length=100, verbose_name='用户名')
    password = models.CharField(default='',max_length=100, verbose_name='密码')
    address = models.CharField(default='',max_length=500, verbose_name='地址')
    phone = models.CharField(default='',max_length=200, verbose_name='电话号码')
    money = models.IntegerField(default=0, verbose_name='金额')

    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return self.name+','+self.username



class Book(models.Model):

    class Meta:
        verbose_name_plural = verbose_name = "图书"

    num = models.CharField(max_length=100,verbose_name='书号')
    name = models.CharField(max_length=100, verbose_name='书名')
    brief = models.CharField(max_length=100, verbose_name='简介')
    author = models.CharField(max_length=100, verbose_name='作者')
    image = models.ImageField(upload_to='books/image/',verbose_name='封面')
    price = models.IntegerField(verbose_name='价格')
    count = models.IntegerField(verbose_name='库存')

    
    def __str__(self):
        return self.num+','+self.name


class Bill(models.Model):

    class Meta:
        verbose_name_plural = verbose_name = "订单"

    buyer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='下单人')
    book = models.ForeignKey(Book,on_delete=models.CASCADE,verbose_name='购买书籍')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='下单时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='批准时间')
    status = models.IntegerField(default=0, choices=[(0, '未审批'), (1, '已批准')],verbose_name='订单状态')

    def __str__(self):
        return self.User.name+','+self.Book.num+','+self.Book.name+','+self.Book.price


>>>>>>> origin/master

