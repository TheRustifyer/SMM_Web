from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        
        if form.is_valid():
            form.save()
        return redirect('/') # Lo mandamos a la página de inicio logueado.

    else:
        form = RegisterForm()

    return render(response, 'z_login_register/register.html', {'active_tab': "register",'form':form})


# def login(response):
#     return render(response, 'z_login_register/login.html', {'active_tab': "login"})

def logout(response):
    return redirect('/')

