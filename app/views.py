from django.shortcuts import render

def first(request):
    return render(request,'first.html')

def login(request):
    return render(request,'login.html')    