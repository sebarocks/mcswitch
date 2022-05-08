from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import boto3
import os

ec2 = boto3.resource('ec2')

INSTANCE_ID = os.environ.get('INSTANCE_ID')

EC2_STATE = {
    0 : 'pending',
    16 : 'running',
    32 : 'shutting-down',
    48 : 'terminated',
    64 : 'stopping',
    80 : 'stopped'
}

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

def index(request):
    if request.user.is_authenticated:
        instance = ec2.Instance(INSTANCE_ID)
        status = instance.state
        context = {
            'user' : request.user.username,
            'estado': EC2_STATE[status['Code']],
            'statuscode': status['Code']
        }

        return render(request,"dashboard.html",context)
    else:
        return redirect('/login')


def encender(request):
    if request.user.is_authenticated and request.method == 'POST':
        instance = ec2.Instance(INSTANCE_ID)
        res = instance.start()
        return redirect('encendido')
    else:
        return HttpResponse("Pero que hace? ud no esta autorizado xD")

def apagar(request):
    if request.user.is_authenticated and request.method == 'POST':
        instance = ec2.Instance(INSTANCE_ID)
        res = instance.stop()
        return redirect('apagado')
    else:
        return HttpResponse("Pero que hace? ud no esta autorizado xD")

def apagado(request):
    return render(request,'apagado.html')

def encendido(request):
    return render(request,'encendido.html')