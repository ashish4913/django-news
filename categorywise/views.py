from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import news
from django.core.files.storage import FileSystemStorage
from category.models import category
from subcategory.models import subcategory
# Create your views here.
def addcatnews(request):
    s=subcategory.objects.all()
    c=category.objects.all()
    if request.method=='POST':
        newstitle=request.POST.get('newstitle')
       
        writer=request.POST.get('writer')
        brief=request.POST.get('brief')
        newsdetails=request.POST.get('newsdetails')
        pubdate=request.POST.get('pub_date')
        cat=request.POST.get('cat') 
        subcat=request.POST.get('subcat')       
        #print(newstitle,newscat,writer,newsdetails)
        if newstitle=="" or writer=="" or newsdetails=="" or pubdate=="" or cat=="" or subcat=="" or brief=="":
            error="All feilds are required"
            return render(request,"back/error.html",{'error':error})
        #to check file is uploaded or not
        image=request.FILES['image']
        f=FileSystemStorage()
        filename=f.save(image.name,image)#set name of image and if already present set some random name
        #url=f.url(filename)#make urls for media folder
        try:
            if str(image.content_type).startswith("image"):#to check the type of file uploaded
                if image.size<5000000:#to check the size of image uploaded
                    catid=subcategory.objects.get(subcat=subcat).catid
                    
                    n=news(about=newstitle,img=image,title=newstitle,imgname=filename,pub_date=pubdate,details=newsdetails,writer=writer,views=0,cat=cat,subcat=subcat,catid=catid,brief=brief)
                    n.save()
                    return redirect(news_list)
                    
                else:
                    
                    f.delete(filename)
                    error="file is too large only support 5MB"
                    return render(request,"back/error.html",{'error':error})

            else:
                f.delete(filename)
                error="file is too large only support 5MB"

                error="File type not supported"
                return render(request,"back/error.html",{'error':error})

                    
        except:
            
            error="please upload image"
            return render(request,"back/error.html",{'error':error})





    return render(request,'back/catnewsadd.html',{'cat':c,'subcat':s})

def news_list(request):
    n=news.objects.all()

    return render(request,"back/catnews_list.html",{"n":n})