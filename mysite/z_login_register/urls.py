from django.urls import path, include
from . import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout),
    path('', include("django.contrib.auth.urls")), # This are for pointing the auth table on migrated external db.   
]