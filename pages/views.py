from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
  return HttpResponse("<h1>Hello, World, Vincent!</h1>")
  