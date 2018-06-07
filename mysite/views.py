from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
	#https://picsum.photos/800/600/?random
    return render(request, "/mysite/mysite/index.html")