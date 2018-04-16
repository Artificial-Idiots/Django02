"""Django02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from app02 import views

urlpatterns = [
    # url(r'^index$', views.index),
    url(r'^index$', views.index, name='index'),

    # 进入模板继承演示界面
    url(r'^inherit$', views.inherit, name='inherit'),

    # 进入登录界面
    url(r'^login$', views.login),

    # 处理登录操作
    url(r'^do_login$', views.do_login),

    # 进入发帖界面
    url(r'^post$', views.post),

    # 处理发帖操作
    url(r'^do_post$', views.do_post),

    # 验证码生成
    url(r'^create_verify_code$', views.create_verify_code),

    # 验证码显示
    url(r'^show_verify_code$', views.show_verify_code),

    # 校验验证码
    url(r'^do_verify$', views.do_verify)

]
