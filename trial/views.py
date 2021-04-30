from django.shortcuts import render
from .forms import Trial_registration
# Create your views here.
def trial_add(request):
    if request.method=='POST':
        fm=Trial_registration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=Trial_registration()

    return render(request,'addandshow.html',{'form':fm})