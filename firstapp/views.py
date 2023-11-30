import json
from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Employee

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

def greeting(request):
    employees = Employee.objects.all()
    employee_list = []
    for employee in employees:
        employee_list.append(employee.name)
    context={'employee':employee_list}
    print(context)
    return render(request,'firstapp/index.html',context)