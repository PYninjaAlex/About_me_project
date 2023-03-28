from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('database', DatabaseRealisation.as_view()),
    path('database/add_users', AddUsers.as_view(), name='add_users'),
]