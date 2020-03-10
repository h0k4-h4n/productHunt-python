from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        #signup action
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'err': 'Username has already been taken'})
            except User.DoesNotExist as exc:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'err': 'Passwords must match'})
    else:
        #signup page
        print()
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #TODO redirect to homepage and logout
    return render(request, 'accounts/logout.html')