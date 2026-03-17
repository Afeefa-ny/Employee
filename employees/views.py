
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm



from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_employees(request):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)
def employee_list(request):
    query = request.GET.get('q')
    dept = request.GET.get('dept')

    employees = Employee.objects.all()

    if query:
        employees = employees.filter(name__icontains=query)

    if dept:
        employees = employees.filter(department__icontains=dept)

    return render(request, 'list.html', {'employees': employees})


def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'form.html', {'form': form})


def employee_detail(request, id):
    emp = get_object_or_404(Employee, id=id)
    return render(request, 'detail.html', {'emp': emp})


def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('list')

def update_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=emp)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'form.html', {'form': form})