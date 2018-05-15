from django.contrib import admin
from django.contrib.auth.models import User as AdminUser, Group
from .models import User
# Register your models here.

admin.site.site_header = '图书销售系统管理后台'
admin.site.site_title = '管理后台'

admin.site.unregister(AdminUser)
admin.site.unregister(Group)
admin.site.register(User)
