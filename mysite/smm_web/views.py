from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, 'smm_web/home.html')

def product(response):
    return render(response, 'smm_web/producto.html')

def dashboard(response):
    url = response.build_absolute_uri()
    tab_name = url.strip('/').split('/')[-1]
    return render(response, 'smm_web/dashboard.html',{'tab_name': tab_name})

def subscripciones(response):
    url = response.build_absolute_uri()
    tab_name = url.strip('/').split('/')[-1]
    return render(response, 'smm_web/dashboard/subscripciones.html', {'tab_name': tab_name})

def productos(response):
    url = response.build_absolute_uri()
    tab_name = url.strip('/').split('/')[-1]
    return render(response, 'smm_web/dashboard/productos.html', {'tab_name': tab_name})

def mi_perfil(response):
    url = response.build_absolute_uri()
    tab_name = ' '.join([word.capitalize() for word in url.strip('/').split('/')[-1].split('_')]) # Just playing :)
    return render(response, 'smm_web/dashboard/mi_perfil.html', {'tab_name': tab_name})

def estadisticas(response):
    return render(response, 'smm_web/dashboard/estadisticas.html', {'tab_name': 'estadísticas'})

def dispositivos(response):
    url = response.build_absolute_uri()
    tab_name = url.strip('/').split('/')[-1]
    return render(response, 'smm_web/dashboard/dispositivos.html', {'tab_name': tab_name})


