from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from .forms import RegisterUserForm
# Create your views here.

def loginUser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('forums')
        else:
            messages.success(request, ("There was an error logging in."))
            return redirect('login')
    else:
        return render(request, 'userPages/login.html', {})
    
def logoutUser(request):
    logout(request)
    messages.success(request, ("Logged out successfully."))
    return redirect('forums')

def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("Registration successful"))
            return redirect('forums')
    else:
        form = RegisterUserForm()

    return render(request, 'userPages/register.html' ,{'form':form})


