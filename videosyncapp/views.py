from django.shortcuts import render, redirect
from .forms import CreateGroup
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html', {'page': 'index', 'include': 'index.html'})

def watchtogether(request, pk):
    return render(request, 'watchtogether.html', {'page':'watchtogether','grpcode':pk})

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