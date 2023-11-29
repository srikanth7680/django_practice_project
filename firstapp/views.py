import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(request):
    return HttpResponse("Good Afternoon This is string Datatype")
def html(request):
    return  HttpResponse('<html><body><h1>Hello!! This is HTML datatype </html></body></h1>')
def jsondata(request):
    json_object = json.dumps({'msg':"Good afternoon This is JSON data"})
    return HttpResponse(json_object)
def dict(request):
    return HttpResponse({'msg':"This is dictionary datatype"})