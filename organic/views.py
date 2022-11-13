
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .form import oganicUpdate
from .models import organic as org
from inorganic.models import inorganic as inorg
# Create your views here.

@login_required(login_url='auth/login')
def home(request):

    return render(request,'home.html')


@login_required(login_url='auth/login')
def organic(request):
       
    org_compounds=org.objects.all()
    inorg_compounds=inorg.objects.all()

    # mergeobj = org_compounds.union(inorg_compounds)
    # mergeobj=list(chain(org_compounds, inorg_compounds))


    return render(request,'datatable.html',{'elems':org_compounds,'catagoryname':'organic'})


def update(request,id):   
    org_compounds=org.objects.all()

    update_element=org.objects.get(id=id)
    form=oganicUpdate(request.POST or None,instance=update_element)
    if form.is_valid():
        form.save()
        return redirect('/organic',{'elems':org_compounds,'catagoryname':'organic'})


    return render(request,'update.html',{'form':form,'element':update_element})
   



def delete(request,id):   
    
    element=org.objects.get(id=id)
    compound=element.name
    catagoryname='organic'
    if request.method=='POST':
        element.delete()
        return redirect('/organic')
    return render(request,'delete.html',{'catagoryname':catagoryname,'compound':compound})

  

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        company=request.POST['company']
        qty=request.POST['qty']
        price=request.POST['price']
        data_added=org(name=name,company=company,qty=qty,price=price)
        data_added.save()
        
        org_compounds=org.objects.all()
        return render(request,'datatable.html',{'elems':org_compounds, 'catagoryname':'organic'})

    return render(request,'addform.html')

def organicsearch(request):
    result=None
    query=None
    query=request.GET['query']
    result=org.objects.filter(name__contains=query)
    return render(request,'datatable.html',{'query':query,'elems':result,'catagoryname':'organic'})
