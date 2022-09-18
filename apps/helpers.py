# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from functools import wraps

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
