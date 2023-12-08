from firstapp.serializers import EmployeeListSerializer
from firstapp.models import Employee
from rest_framework import generics

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer

class EmployeeRetrieve(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer