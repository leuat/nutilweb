from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Execute NUTIL stuff. ")
# Create your views here.
