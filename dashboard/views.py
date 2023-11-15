from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Hehe')


def staff(request):
    return HttpResponse('XD')
