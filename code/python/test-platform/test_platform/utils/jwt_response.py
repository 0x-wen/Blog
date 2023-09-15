# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 00:36
# @Author  : Jw
# @File    : jwt_response.py
from users import serializers


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }

    """
    # return {
    #     'user_id': user.id,
    #     'username': user.username,
    #     'token': token
    # }
    user_serializer = serializers.UsersLoginResponseSerializer(user, context={'request': request})

    response = {'user_id': user_serializer.data.get("id"),
                'username': user_serializer.data.get('username'),
                'token': token}
    return response
