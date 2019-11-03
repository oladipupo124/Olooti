from django.urls import path
from . import views

urlpatterns = [
    path("/bookings", views.Event.as_view())
]