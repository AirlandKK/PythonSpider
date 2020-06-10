"""lagou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from pyjobs.views import IndexView, CiyunView, FenxiView, Ciyun2View


urlpatterns = [
    # path('admin/', admin.site.urls),
    # 首页路由
    path('', IndexView.as_view()),
    # 词云1路由
    path('ciyun/', CiyunView.as_view()),
    # 词云2路由
    path('ciyun2/', Ciyun2View.as_view()),
    # 数据分析路由
    path('fenxi/', FenxiView.as_view()),
]
