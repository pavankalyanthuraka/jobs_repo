from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first_view(request):
    return HttpResponse('<h1>first view response </h1>')
def second_view(request):
    return HttpResponse('<h1>second view respomse</h1>')
def third_view(request):
    return HttpResponse('<h1>third view response</h1>')
