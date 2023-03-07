from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django import forms

from .models import User

#APP FOR AUTH

class SignInForm(forms.Form):
    required_css_class = 'sign_in_form'
    name = forms.CharField(widget = forms.TextInput(attrs = {'class':'form_field username', 'required': 'True', 'placeholder':'Name'}),max_length=32,label = '', required=False)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'form_field password', 'required': 'True', 'placeholder':'Password'}), required= False, label = '')
    
    class Meta:
        model = User

class SignUpForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs = {'class':'form_field username', 'required': 'True', 'placeholder':'Name'}),max_length=32,label = '', required=False)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'form_field password', 'required': 'True', 'placeholder':'Password'}), required= False, label = '')
    confirmPassword = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'form_field password', 'required': 'True', 'placeholder':'Confirm Password'}), required= False, label = '')

    class Meta:
        model = User

def index(request): #signing IN page
    form = SignInForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = request.POST.get("name")
            password = request.POST["password"]
            user = authenticate(request, username = name, password = password)
            if user is not None:
                login(request,user)
                return redirect('scheduleapp:index')
            else:
                messages.error(request,"Invalid user! Check if the username and/or password is correct." )
                return render(request, "accounts/signin.html", {
                'form':form
            })
    context = {'form':form}
    return render(request, 'accounts/signin.html', context)

def signup(request): #CREATING AN ACCOUNT
    form = SignUpForm(request.POST)
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]
        if confirmPassword != password:
            messages.error(request, "Passwords should match")
            return render(request, "accounts/signup.html", {"msg" : "Passwords should match.", 'form':form})
        else:
            if User.objects.filter(username = name):
                messages.error(request, "This name already taken. Please, choose another one.")
                return render(request, "accounts/signup.html", {'form':form})
            else:
                messages.success(request, "Congratulations, you have created the account successfully!")
                user = User.objects.create_user(username = name, password = password)
                user.save()
                return HttpResponseRedirect(reverse("accounts:index"))
    context = {'form':form}
    return render(request, "accounts/signup.html", context)  

def signout(request):
    logout(request)
    return redirect("accounts:index")