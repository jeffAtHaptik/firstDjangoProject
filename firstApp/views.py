from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Employee


def index(request):
    return HttpResponse("Hello, world. You're at the firstApp index.")

def detail(request,employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)

    except Employee.DoesNotExist:
        raise Http404("Employee doesn't exist")
    return HttpResponse(employee)

def companywiseemplyee(request, company_id):
    try:
        employees = Employee.objects.filter(company__id=company_id)
        employee_list = list(employees)
        data = {"results": list(employees.values("employee_name", "company__company_name", "employee_age"))}

    except Employee.DoesNotExist:
        raise Http404("Employee doesn't exist")
    return JsonResponse(data, safe=False)
