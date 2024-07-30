from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Items
from FoodApp.forms import ItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    item_list=Items.objects.all()
    context={
        'item_list':item_list
    }
    return render(request,'FoodApp/home.html',context)

def details(request,item_id):
    item_list=Items.objects.get(pk=item_id)
    context={
        'item_list':item_list
    }
    return render(request,'FoodApp/details.html',context)

def add_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('FoodApp:home')
    return render(request,'FoodApp/item-form.html',{'form':form})

def update_item(request,id):
    item=Items.objects.get(pk=id)
    form=ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('FoodApp:home')
    return render(request,'FoodApp/item-form.html',{'form':form})

def delete_item(request,id):
    item=Items.objects.get(pk=id)
    if request.method=='POST':
        item.delete()
        return redirect('FoodApp:home')
    return render(request,'FoodApp/delete_msg.html',{'item':item})




