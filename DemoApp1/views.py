from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse("<h1 style='color:blue;'>hello from demoapp1,f1()</h2><hr />")

def f2(request):
    return HttpResponse("<h1 style='color:deeppink;'>hello from demoapp1,f2()</h2><hr />")

def home(request):
    return HttpResponse("<center><h1 style='color:violet';'background color:pink;'>welcome to home page</h1></center>")
