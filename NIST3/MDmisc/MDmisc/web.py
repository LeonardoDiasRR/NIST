#!/usr/bin/python
# -*- coding: UTF-8 -*-



from .string import split_r

def URL_params_to_dict( url ):
    return dict( [ ( key, value ) for key, value in split_r( [ '&', '=' ], url ) ] )
