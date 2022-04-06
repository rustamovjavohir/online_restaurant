import jwt

from .models import User
from .serializers import UserSerializers
from rest_framework.exceptions import AuthenticationFailed


def admin(user):
    if user.is_staff:
        users = User.objects.all()
        users_ser = UserSerializers(users, many=True)
        return users_ser.data
    return None


def check_token(request):
    if request.COOKIES.get('Token'):
        token = request.COOKIES.get('Token')
    else:
        token = request.data.get("Token",)
    # token = request.data.get("Token",)
    if not token:
        raise AuthenticationFailed('Unauthenticated')
    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')
