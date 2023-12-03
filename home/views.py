from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def myDjangoProject(request):
    peoples = [
        {'name':'Suraj Saha', 'age':27},
        {'name':'Anindita Bose', 'age':20},
        {'name':'Chandryee KUndu', 'age':42},
        {'name':'Urmila Dey', 'age':23},
    ]
    return render(request, "index.html", context={'peoples':peoples})