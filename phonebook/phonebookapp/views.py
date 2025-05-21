from django.shortcuts import render
from.models import phonebook1

# Create your views here.
def phn(request):
    return render(request,'home.html')

def addnumber(request): 
    phndic={}
    try:
            name=request.POST['name']
            phnnumber=int(request.POST['number'])
            list1=phonebook1.objects.filter(Name=name)
            if list1.exists():
                phndic['msg']='already exists'
                return render(request,'home.html',phndic)
            else:
                emplist=phonebook1(Name=name,Number=phnnumber)
                emplist.save()
                phndic['msg']='name and phone number added'
                return render(request,'home.html',phndic)
    except Exception as b:
            print(b)
            phndic['msg']='name is not addaed'        
            return render(request,'home.html',phndic)
    

def display(request):
    empdtls=phonebook1.objects.all()
    return render(request,'home.html',{'emp':empdtls})

def update(request):
    try:
        oldname=request.POST['oldname']
        newname=request.POST['newname']
        if oldname==newname:
            return render(request,'index.html',{'key':'already exits'})
        phonebook1.objects.filter(Name=oldname).update(Name=newname)
        return render(request,'home.html',{'key':'updated'})
    except Exception as b:
         print(b)
         return render(request,'home.html',{'key':'not upadted'})
          
def delete(request):
     try:
          dlt=request.POST['dlt']
          phonebook1.objects.filter(Name=dlt).delete()
          return render (request,'home.html',{'del':'deleted'})
     except Exception as b:
         print(b)
         return render(request,'home.html',{'del':'not done'})
     

               
