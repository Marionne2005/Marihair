from tkinter.font import names

from django.contrib import admin
from django.urls import path
from .views import service, home, story, reservation_us, reserver_service, add_new_service

urlpatterns = [
    path('',home,name='home'),
    path('services',service,name='servapp'),
    path('story',story,name='storyapp'),
    path('match',reservation_us,name='reservation'),
    path('stick',add_new_service,name='service'),
    path('back-end',reserver_service,name='back-end'),
]
