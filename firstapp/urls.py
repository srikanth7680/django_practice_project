from django.urls import path

from firstapp.views import string,html,jsondata,dict,greeting

urlpatterns = [
    path('string',string),
    path('html',html),
    path('jsondata',jsondata),
    path('dict',dict),
    path('greeting',greeting)
]