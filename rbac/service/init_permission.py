# -*- coding: utf-8 -*-
from django.conf import settings


def init_permission(request, current_user):
    """
    用户权限的初始化
    :param request:
    :param current_user:
    :return: permission_list
    """
    # 根据当前用户信息获取此用户所拥有的所有权限，并放入session。

    # 当前用户所有权限
    permission_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__id",
                                                                                      "permissions__url").distinct()
    # 获取权限中所有的URL
    # permission_list = []
    # for item in permission_queryset:
    #     permission_list.append(item['permissions__url'])

    permission_list = [item['permissions__url'] for item in permission_queryset]
    # 进行解耦的优化引入配置文件
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    return permission_list
