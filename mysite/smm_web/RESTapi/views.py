from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from ..models import AuthUser
from .serializers import AuthExternalApp


from rest_framework import permissions
from rest_framework.views import APIView


class ApiIndexView(APIView):
       permission_classes = (permissions.AllowAny,)

       def post(self, request, pk, format=None):
           return Response("ok")

class UserDataAPIView(generics.ListAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthExternalApp

class RetrieveUserDataAppAPIView(generics.RetrieveAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthExternalApp
    lookup_field = 'pk'


class CustomAuthToken(ObtainAuthToken):
    permission_classes = (permissions.AllowAny,) # Do we need this?

    # Go ahead and check if api/api-auth-token is valid or need only api-auth-token.

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })