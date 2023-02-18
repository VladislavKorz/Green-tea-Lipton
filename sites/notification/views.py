from django.shortcuts import render, redirect, HttpResponse
from .tasks import *
from django.contrib.auth.decorators import login_required

@login_required
def testUrl(request):
    context = absence(1)
    return HttpResponse(str(context))
