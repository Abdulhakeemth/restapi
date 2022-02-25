#from django.db.models.query import QuerySet
from django.shortcuts import render
#from rest_framework import pagination
#from rest_framework import serializers
#from rest_framework import permissions
from rest_framework.response import Response
from .serializers import  UserRegister,UserDataSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
#from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import Http404
# from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

# Create your views here.
class register(APIView):
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,Create=Token.objects.get_or_Create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)        
class login(APIView):
     permission_classes=(IsAuthenticated,) 
           
class welcome(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)

class UserDetails(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
            
        except:
            raise Http404("Given query not found....")

    def Get(self,request,pk,format=None):
        UserData=self.get_object(pk)
        serializer=UserDataSerializer(UserData)
        return Response(serializer.data)

    def Put(self,request,pk,format=None):
        UserData=self.get_object(pk)
        serializer=UserDataSerializer(UserData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message':'error','error':serializer.errors})  

    def Delete(self,request,pk,format=None):
        UserData=self.get_object(pk)
        UserData.delete()
        return Response({'message':'Sorry for User Deleted'})


    