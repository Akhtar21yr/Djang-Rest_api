from django.urls import path
from .views import *

urlpatterns = [
    path('', UserView.as_view()),
    path('<int:pk>', UserViewP.as_view()),
]