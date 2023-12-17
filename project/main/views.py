from django.shortcuts import render
from main.models import Client
from main.serializers import ClientSerializer,LoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework import status

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    
class LoginClient(APIView):
    serializer_class = LoginSerializer
    
    def post(self,request):
        username = request.data.get('username',None)
        password = request.data.get('password',None)
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request=request,user=user)
            return Response('successfully login in system',status=status.HTTP_200_OK)
        return Response('error datas',status=status.HTTP_404_NOT_FOUND)
        