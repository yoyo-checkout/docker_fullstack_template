from django.urls import path
from MainApp.views import MainApi

urlpatterns = [
    path('', MainApi),
]
