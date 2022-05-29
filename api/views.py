from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *


@api_view(['GET'])
def test(request):
    return Response({
        "msg": "Working"
    })


@api_view(['POST', 'GET'])
# @parser_classes([MultiPartParser])
def register_app(request):
# @permission_classes([IsAuthenticated])
    # try:
    
    return Response({
        'msg': 'It worked!'
    })
    
    
    # if request.method == "POST":
    #     print(request.data)

    #     user_ins = User(
    #         username = request.data['full_name'],
    #         email = request.data['email']
    #     )

    #     user_ins.set_password(request.data['password'])
    #     user_ins.save()

    #     User_info.objects.create(
    #         user = user_ins,
    #         phone_number = request.data['phone'],
    #         district = request.data['district'],
    #         address = request.data['address'],
    #             # profile_pic = request.data['profile_pic']
    #     )

    #     return Response({
    #         'status': status.HTTP_201_CREATED,
    #         'msg': 'User created successfully!'
    #     })

    # except Exception as e:
    #     return Response({
    #         'status': status.HTTP_400_BAD_REQUEST,
    #         # 'msg': str(e.error)
    #         'msg': 'Something went wrong!'
    #     })


@api_view(['POST'])
def login_app(request):
    try:
        pass
    
    except Exception as e:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(e.error)
        })
