from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .form import inoganicUpdate

from .models import inorganic as inorg


# Create your views here.


@login_required(login_url='auth/login')
def inorganic(request):
    inorg_compounds=inorg.objects.all()
    return render(request,'datatable.html',{'elems':inorg_compounds,'catagoryname':'inorganic'})

def update(request):

    return render(request,'update.html')



def update(request,id):   
    inorg_compounds=inorg.objects.all()

    update_element=inorg.objects.get(id=id)
    form=inoganicUpdate(request.POST or None,instance=update_element)
    if form.is_valid():
        form.save()
        return redirect('/inorganic',{'elems':inorg_compounds,'catagoryname':'inorganic'})


    return render(request,'update.html',{'form':form,'element':update_element})
   



def delete(request,id):   
    
    element=inorg.objects.get(id=id)
    compound=element.name
    catagoryname='inorganic'
    if request.method=='POST':
        element.delete()
        return redirect('/inorganic')
    return render(request,'delete.html',{'catagoryname':catagoryname,'compound':compound})

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        company=request.POST['company']
        qty=request.POST['qty']
        price=request.POST['price']
        data_added=inorg(name=name,company=company,qty=qty,price=price)
        data_added.save()
        
        inorg_compounds=inorg.objects.all()
        return render(request,'datatable.html',{'elems':inorg_compounds, 'catagoryname':'inorganic'})

    return render(request,'addform.html')

def inorganicsearch(request):
    result=None
    query=None
    query=request.GET['query']
    result=inorg.objects.filter(name__contains=query)
    return render(request,'datatable.html',{'query':query,'elems':result,'catagoryname':'inorganic'})
