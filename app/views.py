from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ToDoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        todo = ToDo.objects.filter(user=user)
        serializer = ToDoSerializers(todo, many=True)
        return Response({
            'status': True,
            'data': serializer.data,
            'message': 'todo fetch successfully'
        })

    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['user'] = user.id
            serializer = ToDoSerializers(data=data)

            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'invalid fields',
                    'data': serializer.errors
                })

            serializer.save()
            return Response({
                'status': True,
                'message': 'Created',
                'data': serializer.data
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'something wrong',
                'data': {}
            })

    def patch(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                    'status': False,
                    'message': 'UID IS REQUIRED',
                    'data': {}
                })

            obj = ToDo.objects.filter(uid=data.get('uid'))
            if not obj.exists():
                return Response({
                    'status': False,
                    'message': 'INVALID UID',
                    'data': {}
                })

            serializer = ToDoSerializers(obj[0], data=data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'invalid fields',
                    'data': serializer.errors
                })
            serializer.save()
            return Response({
                'status': True,
                'message': 'Created',
                'data': serializer.data
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'something wrong',
                'data': {}
            })


