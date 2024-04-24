from django.shortcuts import render
from django.http import HttpResponse
from student.form import Dept_form
from student.models import Department,Student
# Create your views here.
def student(request):
    return render(request,'stu/home.html')
def about_st(request):
    return render(request,'stu/about.html')
def contact_st(request):
    return render(request,'stu/contact.html')

def add_depart(request):
    if request.method=='POST':
        frm=Dept_form(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponse('successfully added')
        else:
            return HttpResponse('error')
    else:
        fm=Dept_form
        return render(request,'stu/add_dept.html',{'form':fm})
    

def add_studnt(request):
    if request.method=='POST':
        d=request.POST['dpt']
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        p=request.POST['ph']
        e=request.POST['em']
        dp=request.POST['dp']
        d_id=Department.objects.get(id=d)
        stu=Student.objects.create(dept_id=d_id,first_name=f_name,last_name=l_name,email=e,phone=p,pic=dp)
       
        stu.save()
        return HttpResponse('successfully saved')
    else:
        data=Department.objects.all()
        return render(request,'stu/add_stud.html',{'dpt':data})

def view_stud(request):
    data=Student.objects.all().select_related('dept_id')
    print(data)
    return render(request,'stu/view_std.html',{'data':data}) 

def del_stud(request,d):
    dec=Student.objects.get(id=d)
    dec.delete()
    return HttpResponse('successfully deleted')