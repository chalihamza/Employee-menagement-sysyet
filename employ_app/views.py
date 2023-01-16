from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from .models import Employee, Role, Department
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'home.html')


def all_employ(request):
    employ = Employee.objects.all()
    data = {
        'employ': employ,
    }
    print(data)
    return render(request, 'all_employ.html', data)


def add_employ(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        # hire_date = request.POST['hire_date']
        emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,
                       dept_id=dept, role_id=role, hire_date=datetime.now())
        emp.save()
        messages.success(request, 'Employee added Successfully')
        return render(request, 'home.html')
    elif request.method == 'GET':
        return render(request, 'add_employ.html')
    else:
        return render(request, 'add_employ.html')


def remove_employ(request, emp_id=0):
    if emp_id:
        try:
            emp_to_remove = Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("Employee Removed successfully!")
        except:
            return HttpResponse("Please enter a valid EMP id")
    emplo = Employee.objects.all()
    data = {
        'emplo': emplo,
    }
    return render(request, 'remove_employ.html', data)


def filter_employ(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        print(emps)
        return render(request, 'all_employ.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_employ.html')
    else:
        return HttpResponse('An Exception Occurred')
