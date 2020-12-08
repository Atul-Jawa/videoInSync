from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def CustomSignUpView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():  
            image = request.FILES['image']
            user = form.save(image)
            login(request, user)
            messages.success(request, "You are logged in successfully!!! ")
            return redirect('/')
        else:
            return render(request, 'account.html', {'page':'register', 'include': 'signup.html', 'form': form})
    else:
        form = CustomUserCreationForm()
        print(form)
        return render(request, 'account.html', {'page':'register', 'include': 'signup.html', 'form': form})

def CustomLoginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                messages.success(request, "You are logged in successfully!!! ")
                return redirect('/')
            else:
                return render(request, 'account.html', {'page':'login', 'include': 'signin.html', 'form': form})
        else:
            return render(request, 'account.html', {'page':'login', 'include': 'signin.html', 'form': form})
    form = LoginForm()
    return render(request, 'account.html', {'page':'login', 'include': 'signin.html', 'form':form })


def signout(request):
    logout(request)
    messages.info(request, "You are logged out successfully!!! ")
    return redirect('/')

