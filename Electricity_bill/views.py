from django.shortcuts import render
from django.http import HttpResponse
from . models import User, Elec_provider, User_electricity, Subscription
from . serializers import UserSerializer, Elec_providerSerializer, User_electricitySerializer, SubscriptionSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def overview(request):
    urls={
        'User_List':'userlist/',
        'User_Detail':'userdetail/<str:pk>/',
        'Add_user':'newuser/',
        'Add_Electricity-provider':'newelec/',
        'Electricity-provider_list':'eleclist/',
        'Update_E-provider':'updateelec/<str:pk>/',
        'User_Reading':'readlist/',
        'Add_UserReading':'newread/',
        'User_Subscription':'sublist/',
        'Add_Subscription':'newsub/',
        'Update_Subscription':'updatesub/',
        'User_bill':'bill/'
    }
    return Response(urls)

@api_view(['GET'])
def userlist(request):
    obj=User.objects.all()
    serializer=UserSerializer(obj, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def userdetail(request,pk):
    obj=User.objects.get(id=pk)
    serializer=UserSerializer(obj, many= False)
    return Response(serializer.data)

@api_view(['POST'])
def newuser(request):
    serializer=UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def newelec(request):
    serializer=Elec_providerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def eleclist(request):
    obj=Elec_provider.objects.all()
    serializer=Elec_providerSerializer(obj, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def updateelec(request,pk):
    obj = Elec_provider.objects.get(id=pk)
    serializer=Elec_providerSerializer(instance=obj,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def readlist(request):
    obj=User_electricity.objects.all()
    serializer=User_electricitySerializer(obj, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def newread(request):
    serializer=User_electricitySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def sublist(request):
    obj=Subscription.objects.all()
    serializer=SubscriptionSerializer(obj, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def newsub(request):
    serializer=SubscriptionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatesub(request,pk):
    obj = Subscription.objects.get(id=pk)
    serializer=SubscriptionSerializer(instance=obj,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def bill(request):
    l,o=[],[]
    for i in User.objects.all():
        s,p,t=0,"",0
        l.append(i.username)
        for j in User_electricity.objects.all():
            if(i.username==str(j.user)):
                s=s+j.reading
        for k in Subscription.objects.all():
            if(i.username==str(k.user)):
                p=str(k.e_provider)
        for m in Elec_provider.objects.all():
            if(p==m.name):
                t=t+m.cost_per_unit
        o.append([i.username,t*s])
    return Response(o)


