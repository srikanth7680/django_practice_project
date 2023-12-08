from rest_framework.serializers import ModelSerializer
from firstapp.models import Employee
class EmployeeListSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name','age','email','joining_date','salary']