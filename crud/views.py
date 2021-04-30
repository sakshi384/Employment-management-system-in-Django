from django.shortcuts import render,redirect
from .forms import employeeRegistration
from .models import emp_details
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q



def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})



# function is for add and show employee

def add_show(request):
    if request.method=='POST':
        fm=employeeRegistration(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm=employeeRegistration()


    # emp_data=emp_details()
    show_data=emp_details.objects.all()
    print(show_data)
    context={'form':fm,'showdata':show_data}

    return render(request,'addandshow.html',context)


# function is for delete employee
def delete_record(request,id):
    if request.method=='POST':
        delete_data=emp_details.objects.get(id=id)
        delete_data.delete()
    return redirect("/")


# function is for update employee
def update_record(request,id):
    instance = emp_details.objects.get(id=id)
    if request.method == 'POST':
        fm=employeeRegistration(request.POST,instance=instance)
        if fm.is_valid():
            fm.save()

    else:
        # pi = emp_details.objects.get(id=id)
        fm = employeeRegistration(instance=instance)
    return render(request,'update.html',{'id':id,'form':fm})


# function is for search the employee
def search_record(request):
    query1 = request.GET.get('q1')
    query2 = request.GET.get('q2')
    object_list = emp_details.objects.filter(
        Q(technology=query1) | Q(location=query2)
    )
    # return object_list
    # context={'query':queryset}

    return render(request,'search.html',{'search_result':object_list})

