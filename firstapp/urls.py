from django.urls import path

from firstapp.views import string,html,jsondata,dict,greeting,employee_template

urlpatterns = [
    path('string',string),
    path('html',html),
    path('jsondata',jsondata),
    path('dict',dict),
    path('greeting',greeting),
    path('employee_template/<int:emp_id>',employee_template)
]