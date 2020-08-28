from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.


def register(request):
    #Kısa yol request kontrolü yapmadan 
    form = RegisterForm(request.POST or None) #GET request geldiği zaman boş form döndürülür 
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla Kayıt Oldunuz ...")
        return redirect("index")

    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    #ikinci yol request kontrolü yaparak
    """
    if request.method == "POST": #Form Kayıt Etme
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username =username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            return redirect("index")
        
        context = {
            "form" : form
        }

        return render(request,"register.html",contex)

    else: #GET request (sayfaya gidiş)
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.html",contex)  
    """
    
 
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı...") 
            return render(request, "login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")


    return render(request,"login.html",context) #Sayfaya giriş

 
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    return redirect("index")

