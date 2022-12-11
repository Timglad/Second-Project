from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import NewUserForm
from users.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


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

@login_required
def single_user(request):
    user = UserProfile.objects.get(user=request.user)

    return render(request,'user.html',{'user':user})

@login_required
def user_menu(request):
    try:
        profile = UserProfile(user=request.user)
        profile.save()
    except:
        user = UserProfile.objects.get(user=request.user)
    if request.method == "GET":
        return render(request,'user.html',{'user':user,'edit':True})
    user.fullname = request.POST.get('fullname')
    user.city = request.POST.get('city')
    user.age = request.POST.get('age')
    user.image = request.POST.get('image')
    user.save()
    messages.info(request,"Saved Successfuly")

    return redirect('users:showuser')

def first_login(request):
     profile = UserProfile(user=request.user)
     profile.save()
     return redirect('books:mains')

@staff_member_required
def customer_list(request):
    users = UserProfile.objects.all()
    return render(request,'all_users.html',{'users':users})

@staff_member_required
def deluser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('users:customerlist')

    
