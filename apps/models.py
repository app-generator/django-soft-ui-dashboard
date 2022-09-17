# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Add your models here

class Book(models.Model):
    
    # ID is automaticaly handled by Django
    name = models.CharField(max_length=100)