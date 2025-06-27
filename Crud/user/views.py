from django.shortcuts import render , redirect
from django.contrib import messages
from . forms import UserRegistrationForm
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method == 'POST':
        fm=UserRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            username=request.POST['username']
            messages.success(request, f"Account was created Succesfully! Username:{username}")
            return redirect('login')
    
    else:
        fm= UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': fm})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # your protected page
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')