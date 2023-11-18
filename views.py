from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(request):
    std=Student.objects.all()
    return render(request,'student/home.html',{'std':std})
def std_Add(request):
    if request.method=="POST":
        print('added')
        # retreive the user  inputs
        stds_roll=request.POST.get("std_roll")
        stds_name=request.POST.get("std_name")
        stds_email=request.POST.get("std_email")
        stds_phone=request.POST.get("std_phone")
        # create an object for models
        s=Student()
        s.roll=stds_roll
        s.name=stds_name
        s.email=stds_email
        s.phone=stds_phone
        s.save()
        return redirect("/std/home")

    return render(request,'student/add_std.html')
def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/std/home")
def update_std(request,roll):
    std=Student.objects.get(pk=roll)
    return render(request,"student/update_std.html",{'std':std})
def do_update_std(request,roll):
    std_roll=request.POST.get("std_roll")
    std_name=request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_phone=request.POST.get("std_phone")

    std=Student.objects.get(pk=roll)
    std.roll=std_roll
    std.name=std_name
    std.email=std_email
    std.phone=std_phone
    std.save()
    return redirect("/std/home")


