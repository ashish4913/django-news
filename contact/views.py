from django.shortcuts import render
from category.models import category
from categorywise.models import news
from main.models import main
from .models import con

# Create your views here.
def contact(request):

    if request.method=='POST':
        n=request.POST.get('name')
        e=request.POST.get('email')
        w=request.POST.get('website')
        m=request.POST.get('msg')
        
        c=con(name=n,email=e,website=w,msg=m)
        c.save()
        
      
       


    c=category.objects.all()
    catfeature=news.objects.all()
    popnews=news.objects.all().order_by('-views')[0:3]
    site=main.objects.get(title="Magnews")
    d={'site':site,'cat':c,'news':catfeature,'popnews':popnews}
    return render(request,"contact.html",d)
