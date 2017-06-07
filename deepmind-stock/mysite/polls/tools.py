# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

#Reset django user passowrd.
#Defaut admin user is 'admin',passowrd is [1-9]
def reset_password(username='admin',password='123456789'):
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
