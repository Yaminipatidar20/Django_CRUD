from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('add/', add, name='add'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
    path('signin/', signin, name='signin'),
    path('register/', register, name='register'),
    path('logout_view/', logout_view, name='logout_view'),
]
