from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import EmployeeForm,ProjectForm
from .forms import forms, LoginForm
from django.views import View
from .models import Employee,Project


# Create your views here.
class index(View):
    def get(self,request):
        template =loader.get_template('Employee/index.html')
        # for i in LoginForm.declared_fields:
        #     print(LoginForm.declared_fields[i].widget.input_type)
        context={
            'login':LoginForm,
            'employee':EmployeeForm,
            'project':ProjectForm
        }
        return HttpResponse(template.render(context,request))
    def post(self,request):

        proj=Project.objects.get(id=request.POST['projcet'])
        emp=Employee()
        emp.projcet = proj
        emp.firstname=request.POST['firstname']
        emp.lastname = request.POST['lastname']

        emp.email=request.POST['email']
        emp.age = request.POST['age']
        emp.mobile = request.POST['mobile']

        emp.save()


        return  HttpResponse(emp.firstname)
class employee_details(View):

    def get(self,request):
        emp=Employee.objects.all()
        data1={
            'data':emp,
            'employee': EmployeeForm,
        }
        template = loader.get_template('Employee/index1.html')

        return HttpResponse(template.render(data1,request))


class Employee_update(View):
    def get(self,request,id):
        emp=Employee.objects.get(id=id)
        empform=EmployeeForm(instance=emp)


    def POST(self, request,id):
        proj =  Employee.objects.get(id=id)
        print(proj)
        user=EmployeeForm(request.POST,instance=proj)
        user.save()
        return redirect('emp')







