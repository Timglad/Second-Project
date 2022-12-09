from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import NewUserForm, UserProfileForm
from users.models import UserProfile


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



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("users:firstlogin")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, "register_form.html", context={"register_form":form})

def logout_func(request):
    
    logout(request)
    return redirect('books:mains')

def user_menu(request):
    current_user = request.user
    user = UserProfile.objects.get(id=current_user.id)
    if request.method == "GET":
        return render(request,'user.html',{'user':user,'edit':True})
    user.fullname = request.POST.get('fullname')
    user.city = request.POST.get('city')
    user.age = request.POST.get('age')
    user.image = request.POST.get('image')
    user.save()
    messages.info(request,"Saved Successfuly")
    return redirect('books:mains')

def first_login(request):
     profile = UserProfile(user=request.user)
     profile.save()
     return redirect('books:mains')