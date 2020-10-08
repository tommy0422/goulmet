from django.urls import path
from .views import reservation_option

app_name = "reservation"

urlpatterns = [
    path('reservation_option/', reservation_option, name='reservation_option'),
]