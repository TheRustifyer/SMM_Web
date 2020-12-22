from rest_framework import serializers

from ..models import AuthUser



class AuthExternalApp(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
            'id',
            'username',
            'password',
        )
from rest_framework.authtoken.models import Token

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')