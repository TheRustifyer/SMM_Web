from rest_framework import routers
from django.urls import path
from .views import UserDataAPIView, CustomAuthToken, ApiIndexView

app_name = 'tkinter_api'

urlpatterns = [
    path('data', UserDataAPIView.as_view()),
    # path('<pk>/', RetrieveUserDataAppAPIView.as_view(), name='retrieve_data'),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('index/', ApiIndexView.as_view()),
]
