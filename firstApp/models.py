from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.TextField(max_length=100)
    company_est_date = models.DateField('Date establishment')

    def __str__(self):
        return self.company_name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.TextField(max_length=100)
    employee_age = models.IntegerField()

    def __str__(self):
        return self.employee_name

