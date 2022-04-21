from django.shortcuts import render, HttpResponse
from django.views.generic import ListView


def list_jokes(request):
    return render(request, "jokes/index.html")
