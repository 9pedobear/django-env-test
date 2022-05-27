from django.shortcuts import render
from django.http import HttpResponse
from .tasks import mail_for_me

def index(request):
    mail_for_me()
    return HttpResponse('Hi')