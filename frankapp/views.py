from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def gkpage(request):
    template = loader.get_template('important.html')
    return HttpResponse(template.render())
