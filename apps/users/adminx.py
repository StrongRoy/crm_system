#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views
from .models import VerifyCode
from .models import UserProfile

class BaseSetting:
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True

class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]



class GlobalSettings:
    site_title = "倚天屠龙刀"
    site_footer = "https://home.cnblogs.com/u/richiewlq/"
    # 菜单收缩
    menu_style = "accordion"

class UserProfileAdmin(object):
    list_display = ['username',"gender",'birthday', 'email', "mobile",]

xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)