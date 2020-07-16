from django.urls import path
from .views import *

urlpatterns = [
    path('', ExpandingMatrix.as_view(), name='expand'),
]