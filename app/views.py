from django.shortcuts import render
from .models import EmployeeModel

# Create your views here.
def home(request):
    return render(request,"index.html")


def addEmployee(request):
    return render(request,"employee.html")


def saveEmployee(request):
    idno=request.POST.get('t1')
    name=request.POST.get('t2')
    des=request.POST.get('t3')
    sal=request.POST.get('t4')
    gender=request.POST.get('t5')
    co=request.POST.get('t6')
    eid=request.POST.get('t7')
    EmployeeModel(idno=idno,name=name,designation=des,salary=sal,gender=gender,contact=co,email=eid).save()
    return render(request,"index.html",{"msg":"Details Saved Successfully"})


def showEmployee(request):
    em=EmployeeModel.objects.all()
    return render(request,"index.html",{"data":em})


def updateEmployee(request):
    idno=request.GET.get("idno")
    print(idno)
    return render(request,"update.html",{"id":idno})


def deleteEmployee(request):
    idno = request.GET.get("idno")
    EmployeeModel.objects.filter(idno=idno).delete()
    return render(request,"index.html",{"msg":"Employee Details Deleted"})