from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

# Create your views here.
def register(response):
    
    if response.method == 'POST':
        form = RegisterForm(data=response.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('/login') # Lo mandamos a la página de inicio ya registrado para que se loguee con las nuevas credenciales

    else:
        form = RegisterForm()

    return render(response, 'z_login_register/register.html', {'active_tab': "register", 'form':form})


def login(response):
    
    form = AuthenticationForm(data=response.POST)
    if response.method == 'POST':
        
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login 'a pedales'...
                do_login(response, user)
                
                if not response.user.is_superuser:
                # Le redireccionamos a la portada
                    return redirect('/dashboard')
                else:
                    return redirect('/admin')
            
    else:
        form = AuthenticationForm()

    return render(response, 'z_login_register/login.html', {'active_tab': "login", 'form':form})

def logout(response):
    do_logout(response)
    return redirect('/login')

