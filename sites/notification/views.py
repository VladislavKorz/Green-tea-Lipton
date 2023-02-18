from django.shortcuts import render, redirect, HttpResponse
from .tasks import *

def testUrl(request):
    context = absence(1)
    return HttpResponse(str(context))
