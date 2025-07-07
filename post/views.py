from django.shortcuts import render
from django.http import HttpResponse

def index(Request):
    return render(Request,'index.html')
    

# Create your views here.
