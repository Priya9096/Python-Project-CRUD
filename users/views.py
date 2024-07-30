from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'users/register.html',{'form':form})

def profile(request):
    return render(request,'users/profile.html')




