"""booksale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views as book_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_views.index),
    path('index', book_views.index),
    path('user/login/', book_views.login),
    path('user/logout/', book_views.user_logout),
    path('search/', book_views.search),

    path('register/',book_views.register),
    path('buy/',book_views.buy),
    path('personal/',book_views.personal),
    path('bills/',book_views.bills),




    path('all/book/', book_views.allbook),
    path('all/notice/', book_views.all_notice),
    path('notice/detail/', book_views.notice_detail),
    path('book/fenlei/', book_views.book_fenlei),
    path('type/detail/', book_views.type_detail),
    path('book/detail/', book_views.book_detail),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
