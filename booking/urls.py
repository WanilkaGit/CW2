from django.urls import path
from booking import views

urlpatterns = [
    path("rooms/", views.room_list, name="room-list"),
    path("book-room/", views.booking_room, name="book-room"),
    path("booking-details/<int:pk>/", views.booking_details, name="booking-details"),
]