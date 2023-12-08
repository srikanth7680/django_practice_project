from django.urls import path

from firstapp.views import string,html,jsondata,dict,greeting,employee_template
from firstapp.apis import EmployeeList
urlpatterns = [
    path('string',string),
    path('html',html),
    path('jsondata',jsondata),
    path('dict',dict),
    path('greeting',greeting),
    path('employee_template/<int:emp_id>',employee_template),
    path('drf/employee',EmployeeList.as_view())
]