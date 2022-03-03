from django.urls import path
from .views import LoginViews, UserViews, RegisterViews, LogoutViews


urlpatterns = [
    path('login/', LoginViews.as_view(), name='login'),
    path('user/', UserViews.as_view(), name='user'),
    path('register/', RegisterViews.as_view(), name='register'),
    path('logout/', LogoutViews.as_view(), name='logout')
]
