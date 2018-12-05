# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100,null=False)
    Password = models.CharField(max_length=50,null=False)
    Sex = models.CharField(max_length=1,null=False)
    Detail = models.CharField(max_length=100,null=False)