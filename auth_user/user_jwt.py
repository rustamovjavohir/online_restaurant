import jwt
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.response import Response
from .models import User


class L_JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request=request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")
        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed("Token not valid ")
        token = auth_token[1]
        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
            id = payload.get('id', None)
            user = User.objects.get(id=id)
            response = Response()
            response.data = {
                "username": user.username,
                "token": token
            }
            return user, token

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed('Token is expired, login again')

        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed('Token is invalid ')
