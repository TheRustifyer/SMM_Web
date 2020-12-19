from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, 'smm_web/home.html')

def product(response):
    return render(response, 'smm_web/producto.html')

