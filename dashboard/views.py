from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response

from dashboard.mcserver import MCQueryController
from dashboard.awscontroller import AWSController


mcAws = AWSController()
mcServer = MCQueryController(mcAws)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,"failed.html")
    return render(request,"login.html")

@login_required
def index(request):
    context = {
        'user' : request.user.username,
        'estado': mcAws.getState(),
        'statuscode': mcAws.getStatusCode(),
        'players': mcServer.players()
    }
    return render(request,"dashboard.html",context)


@login_required
def encender(request):
    if request.user.is_authenticated and request.method == 'POST':
        mcAws.start()
        return redirect('encendido')
    else:
        return redirect('logout')

@login_required
def apagar(request):
    if request.user.is_authenticated and request.method == 'POST':
        mcAws.stop()
        return redirect('apagado')
    else:
        return redirect('logout')

@login_required
def apagado(request):
    return render(request,'apagado.html')

@login_required
def encendido(request):
    return render(request,'encendido.html')

def logoutpage(request):
    logout(request)
    return redirect('index')

@api_view()
def serverState(request):
    mcserverjson = {
        'state': mcAws.getState(),
        'players': mcServer.players()
    }
    return Response(mcserverjson)
