from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *


@api_view(['POST', 'GET'])
@parser_classes([MultiPartParser])
def register_app(request):
# @permission_classes([IsAuthenticated])
    try:
        if request.method == "POST":
            print(request.data['profile_pic'])

            user_ins = User(
                username = request.data['full_name'],
                email = request.data['email']
            )

            user_ins.set_password(request.data['password'])
            user_ins.save()

            User_info.objects.create(
                user = user_ins,
                phone_number = request.data['phone'],
                district = request.data['district'],
                address = request.data['address'],
                profile_pic = request.data['profile_pic']
            )

            return Response({
                'status': status.HTTP_201_CREATED,
                'msg': 'User created successfully!'
            })

    except Exception as e:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(e.error)
        })

@api_view(['POST'])
def login_app(request):
    try:
        try:
            user_info_ins = User_info.objects.get(phone_number=request.data['phone_number'])
            
            if request.data['phone_number'] == user_info_ins.phone_number and user_info_ins.user.check_password(request.data['password']):
                profile_pic = ""

                if user_info_ins.profile_pic.url == "/media/null":
                    profile_pic = '/media/default_avatar.png'
                else:
                    profile_pic = user_info_ins.profile_pic.url
                return Response({
                    'status': status.HTTP_200_OK,
                    'data': {
                        'id': user_info_ins.id,
                        'username': user_info_ins.user.username,
                        'email': user_info_ins.user.email,
                        'phone_number': user_info_ins.phone_number,
                        'district': user_info_ins.district,
                        'address': user_info_ins.address,
                        'profile_pic': profile_pic
                    }
                })    

            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'msg': 'invalid_credentials'
                })            

        except:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'msg': 'invalid_credentials'
            })

    except Exception as e:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(e.error)
        })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_info(request, id):
    if request.method == "GET":
        try:
            user_info_ins = User_info.objects.get(pk=id)
            user_ins = User.objects.get(pk=user_info_ins.user.id)

            return Response({
                'status': status.HTTP_200_OK,
                'data': {
                    'full_name': user_ins.username,
                    'phone_number': user_info_ins.phone_number,
                    'email': user_ins.email,
                    'district': user_info_ins.district,
                    'address': user_info_ins.address
                }
            })

        except Exception as e:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': str(e.error)
            })
    if request.method == "POST":
        try:
            user_info_ins = User_info.objects.get(pk=id)
            user_ins = User.objects.get(pk=user_info_ins.user.id)

            user_ins.username = request.data['full_name']
            user_ins.email = request.data['email']
            user_info_ins.phone_number = request.data['phone']
            user_info_ins.district = request.data['district']
            user_info_ins.address = request.data['address']

            user_info_ins.save()
            user_ins.save()

            return Response({
                'status': status.HTTP_200_OK,
                'msg': 'Data saved!',
                'data': {
                    'full_name': user_ins.username,
                    'phone_number': user_info_ins.phone_number,
                    'email': user_ins.email,
                    'district': user_info_ins.district,
                    'address': user_info_ins.address
                }
            })

        except Exception as e:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': str(e.error)
            })
