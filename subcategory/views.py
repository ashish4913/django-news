from django.shortcuts import render,redirect
from .models import subcategory
from category.models import category
def add_subcat(request):
    c=category.objects.all()
    if request.method=='POST':
        subcat=request.POST.get('subcatname')
        catname=request.POST.get('newscat')
        

        if(subcategory.objects.filter(subcat=subcat)):
       
            error="sub-category already exist"
            return render(request,'back/error.html',{'error':error})
        else:
           
            catid=category.objects.get(cat=catname).catid
            c=subcategory(subcat=subcat,catname=catname,catid=catid)
            c.save()
            return redirect(manage_subcat)

    return render(request,"back/addsubcat.html",{'c':c})

def manage_subcat(request):
    subcat=subcategory.objects.all()

    return render(request,"back/managesubcat.html",{'subcat':subcat})