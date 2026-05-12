from django.urls import path
from .views import *


# /auth/
urlpatterns = [
    # /auth/register/

    path('', auth_view, name='auth'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('my-account/', MyAccountView.as_view(), name='my-account' ),
    path('update-account/', UserUpdateView.as_view(), name='update-account'),
    # my-account
    # update-account
    # change-password
]