from django.urls import path

from .views import list_jokes

app = "jokes"

urlpatterns = [
    path("", list_jokes, name="list-jokes"),
]
