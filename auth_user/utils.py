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
    token = request.COOKIES.get('Token')
    if not token:
        raise AuthenticationFailed('Unauthenticated')
    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')
