from django.shortcuts import render,redirect
from .forms import Adddata
from app.models import vaibhav

# Create your views here.

def home(request):
    
    form_class=Adddata(request.POST or None)
    if form_class.is_valid():
        form_class.save()
        form_class=Adddata()
    return render(request,'home.html',{
        'form':form_class
    })


def edit(request,product_id):
    product=vaibhav.objects.get(id=product_id)

    form_class=Adddata(request.POST or None, instance=product)
    if form_class.is_valid():
        form_class.save()

    return render(request,'edit.html',{
        'form':form_class
        
    })

def list(request):
    products=vaibhav.objects.all()
    return render(request,'list.html',
    {
        "products":products
    })

def delete(request,product_id):
    vaibhav.objects.get(id=product_id).delete()

    return redirect('/list')


