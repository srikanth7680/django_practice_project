from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    is_employed = models.BooleanField(default=True)
    # login_time = models.TimeField(default=True)

