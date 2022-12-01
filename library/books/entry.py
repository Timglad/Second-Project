from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_func(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'USER NOT EXISTS')
            return render(request, 'entry_form.html', {}) 
        
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('books:mains')
        
        else:
            messages.error(request, 'PASSWORD ERROR OCCURRED WHILE LOG-IN') 

    return render(request, 'entry_form.html', {})


def register_func(request):

    if request.method == 'GET':
        form = UserCreationForm()
        return render(request,'register_form.html',{'form':form})
    
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:login_func')
        return render(request,'register_form.html',{'form':form})


def logout_func(request):
    
    logout(request)
    return redirect('books:mains')
