from django.urls import path
from .views import receive_signal

urlpatterns = [
    path('receive_signal/', receive_signal, name='receive_signal'),
]