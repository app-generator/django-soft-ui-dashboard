# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from functools import wraps

from django.db import models
from django.http import HttpResponseRedirect, HttpResponse

def check_permission(function):
    @wraps(function)
    def wrap(viewRequest, *args, **kwargs):

        try:

            # Check user
            if viewRequest.request.user.is_authenticated:
                return function(viewRequest, *args, **kwargs)

            # All good - allow the processing
            return HttpResponseRedirect('/login/')

        except Exception as e:

            # On error
            return HttpResponse( 'Error: ' + str( e ) )

        return function(viewRequest, *args, **kwargs)

    return wrap

class Utils:
    @staticmethod
    def get_class(config, name: str) -> models.Model:
        return Utils.model_name_to_class(config[name])

    @staticmethod
    def get_manager(config, name: str) -> models.Manager:
        return Utils.get_class(config, name).objects

    @staticmethod
    def get_serializer(config, name: str):
        class Serializer(serializers.ModelSerializer):
            class Meta:
                model = Utils.get_class(config, name)
                fields = '__all__'

        return Serializer

    @staticmethod
    def model_name_to_class(name: str):
        all_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        for cls in all_classes:
            if cls[0] == name:
                return cls[1]
        # we are confident that never returns None
        return None
