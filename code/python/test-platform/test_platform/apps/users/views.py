from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import generics, status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from users import serializers


class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UsersRegisterModelSerializer


class UsernameIsExisted(APIView):

    def get(self, request, username):
        count = 0
        if User.objects.filter(username=username).exists():
            count = 1

        return Response({'username': username, 'count': count}, status=status.HTTP_200_OK)


class EmailIsExisted(APIView):

    def get(self, request, email):
        count = 0
        if User.objects.filter(email=email).exists():
            count = 1
        res = {'username': email, 'count': count}
        return Response(res, status=status.HTTP_200_OK)
