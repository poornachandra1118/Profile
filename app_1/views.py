from django.shortcuts import render

# Create your views here.
from .models import *

def Index(req):
    data=Employee_profile.objects.all()
    if req.method=='POST':
        emp_id=req.POST.get('empid')
        emp_name=req.POST.get('empname')
        emp_profile=req.FILES.get('empimage')
        emp_resume=req.FILES.get('empresume')
        print(emp_id,emp_name,emp_profile,emp_resume)
        Employee_profile.objects.create(
            Emp_id=emp_id,
            Emp_name=emp_name,
            Emp_profile=emp_profile,
            Emp_resume=emp_resume
        ).save()
    context={
        'Data':data
    }
    return render(req,'Index.html',context)