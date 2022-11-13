from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .form import solventUpdate

from .models import solvents as solv


@login_required(login_url='auth/login')
def solvents(request):
    solv_compounds=solv.objects.all()
    return render(request,'datatable.html',{'elems':solv_compounds, 'catagoryname':'solvents'})

def update(request):

    return render(request,'update.html')

    
def update(request,id):   
    solv_compounds=solv.objects.all()

    update_element=solv.objects.get(id=id)
    form=solventUpdate(request.POST or None,instance=update_element)
    if form.is_valid():
        form.save()
        return redirect('/solvents',{'elems':solv_compounds,'catagoryname':'solvents'})


    return render(request,'update.html',{'form':form,'element':update_element})
   


def delete(request,id):   
    
    element=solv.objects.get(id=id)
    compound=element.name
    catagoryname='solvents'
    if request.method=='POST':
        element.delete()
        return redirect('/solvents')
    return render(request,'delete.html',{'catagoryname':catagoryname,'compound':compound})



def add(request):
    if request.method=='POST':
        name=request.POST['name']
        company=request.POST['company']
        qty=request.POST['qty']
        price=request.POST['price']
        data_added=solv(name=name,company=company,qty=qty,price=price)
        data_added.save()
        
        solv_compounds=solv.objects.all()
        return render(request,'datatable.html',{'elems':solv_compounds, 'catagoryname':'solvents'})

    return render(request,'addform.html')


def solventssearch(request):
    result=None
    query=None
    query=request.GET['query']
    result=solv.objects.filter(name__contains=query)
    return render(request,'datatable.html',{'query':query,'elems':result,'catagoryname':'solvents'})
