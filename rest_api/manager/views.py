from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.messages import constants as messages
from .models import CustomUser
from .models import transact
from .serializers import transactSerializer
from .serializers import CustomUserSerializer

class CustomUserList(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    # post method for creating a new user
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        balance = request.data.get('balance')
        user = CustomUser.objects.create_user(username, email, balance, password)

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
        
    def delete(self,request):
        CustomUser.objects.all().delete()
        serializer = CustomUserSerializer()
        return Response(serializer.data)
    

class CustomUserDetailView(APIView):
    def get_queryset(self):
        return CustomUser.objects.all()

    def get(self, request, pk):
        user = CustomUser.objects.get(username=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def delete(self,request,pk):
        user = CustomUser.objects.get(username=pk)
        user.delete()
        return Response({"Success"})
    
    def put(self,request,pk):
        user = CustomUser.objects.get(username=pk)
        email = request.data.get('email')
        password = request.data.get('password')
        balance = request.data.get('balance')
        user.delete()
        user = CustomUser.objects.create_user(pk, email, balance, password)
        return Response({"Success"})

class transactList(APIView):
    queryset=transact.objects.all()
    serializer_class = transactSerializer

    def get(self,request):
        transacts = transact.objects.all()
        serializer = transactSerializer(transacts, many=True)
        return Response(serializer.data)
    
class aa(APIView):
    def post(self, request):
        payer = request.data.get('payer')
        payee = request.data.get('payee')
        amount=request.data.get('amount')
        transactid=request.data.get('transactid')
        transact = transact.objects.create_transact(payer,payee,amount,transactid)

        serializer = transactSerializer(transact)
        return Response(serializer.data)
