from django.contrib import admin
from django.contrib.auth.models import User as AdminUser, Group
from .models import User
from .models import *
# Register your models here.

admin.site.site_header = '图书销售系统管理后台'
admin.site.site_title = '管理后台'

admin.site.unregister(AdminUser)
admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Bill)
admin.site.register(Notice)
