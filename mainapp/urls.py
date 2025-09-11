from django.urls import path
from .views import index, snd_hr, fk_db

urlpatterns = [
    path("", index),
    path("snd_hr", snd_hr),
    path("fk_db", fk_db),
]


