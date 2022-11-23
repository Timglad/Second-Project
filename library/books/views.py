from django.shortcuts import render
from django.http import HttpResponse


def mains(request):
    return HttpResponse("it works")
