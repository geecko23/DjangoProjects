from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import Student
from . forms import StudentInfoForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect




def manage(request):
   
    students=Student.objects.all().values()
    return render(request,'manage/manage.html',{'students':students})

@login_required 
def update(request,id):
    if request.method =='POST':
        student=Student.objects.get(pk=id)
        fm=StudentInfoForm(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
    
            return HttpResponseRedirect('/')

    else:

        student=Student.objects.get(pk=id)
        fm=StudentInfoForm(instance=student)
        return render(request, 'manage/stdupd.html',{'form':fm})
    
@login_required 
def delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect('/')

@login_required 
def addstudent(request):
    if request.method == 'POST':
        fm=StudentInfoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
    
        fm=StudentInfoForm()
    return render(request,'manage/add.html',{'form':fm})

@login_required 
def searchstudent(request):
    if request.method == 'POST':
        search = request.POST.get('output')
        student=Student.objects.all()
        std=Student.objects.all()
        if search:
            std=student.filter(
                Q(fname__icontains=search)|
                Q(lname__icontains=search)|
                Q(email__icontains=search)|
                Q(phone__icontains=search)|
                Q(branch__icontains=search)

            )
        return render(request,'manage/manage.html',{'students':std})

    else:
        return HttpResponse('A error occured')