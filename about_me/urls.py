from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('database/', DatabaseRealisation.as_view())
]