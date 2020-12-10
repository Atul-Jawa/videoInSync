from django.shortcuts import render, redirect
from .forms import CreateGroup, CreateGroupgdrive
from django.contrib import messages
from django.urls import reverse
from .models import Group
# Create your views here.
def index(request):
    return render(request, 'index.html', {'page': 'index', 'include': 'index.html'})

def watchtogether(request, pk):
    try:
        group = Group.objects.get(pk=pk)
        return render(request, 'watchtogether.html', {'page':'watchtogether', 'grpcode':pk, 'link':group.link})
    except Group.DoesNotExist:
        return render(request, 'watchtogether.html', {'page':'watchtogether', 'grpcode':pk})

def creategrpgdrive(request):
    if request.method == 'POST' :
        form = CreateGroupgdrive(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            pk = form.save(user).pk
            print(pk)
            messages.success(request, "Group Created Successfully!!")
            #messages.success(request, "Assignment Uploaded Successfully!!")
            return redirect(reverse('watchtogether', kwargs={'pk':pk}))
        else:
            return render(request, 'creategrp.html', {'form':form})
    form = CreateGroupgdrive()
    return render(request, 'creategrp.html', {'page':'creategrp','link':'link', 'form':form})

def creategrp(request):
    if request.method == 'POST' :
        form = CreateGroup(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            pk = form.save(user).pk
            print(pk)
            messages.success(request, "Group Created Successfully!!")
            #messages.success(request, "Assignment Uploaded Successfully!!")
            return redirect(reverse('watchtogether', kwargs={'pk':pk}))
        else:
            return render(request, 'creategrp.html', {'form':form})
    form = CreateGroup()
    return render(request, 'creategrp.html', {'page':'creategrp','form':form})

def joingrp(request):
    return render(request, 'joingrp.html', {'page':'joingrp'})