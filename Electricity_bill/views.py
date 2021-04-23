from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Elec_provider, User_electricity, Subscription
from django.template import loader
from django.db import connection

def Home(request):
    l=[]
    posts = User.objects.all()
    k= User_electricity.objects.raw('Select * from electricity_bill_user_electricity')
    sub = Subscription.objects.all()
    ep=Elec_provider.objects.all()
    for i in posts:
        s,p,t=0,"",0
        for j in k:
            if(i.username==str(j.user)):
                s=s+j.reading
        for m in sub:
            if(i.username==str(m.user)):
                p=str(m.e_provider)
        for n in ep:
            if(p==str(n.name)):
                t+=n.cost_per_unit
        l.append([i.username,t*s])
    return render(request, 'Electricity_bill/output.html', {'data': l})



