from django.shortcuts import render,redirect
from .models import main,Trandingpost
from django.core.files.storage import FileSystemStorage
from category.models import category
from categorywise.models import news
from subcategory.models import subcategory
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    post=Trandingpost.objects.all()
    n=news.objects.all()
    popnews=news.objects.all().order_by('-views')[0:3]
    
    c=category.objects.all()
    s=subcategory.objects.all()
    catfeature=news.objects.all()
    site=main.objects.all()[0]
    d={'site':site,'post':post,'news':n,'cat':c,"f":catfeature,'sub':s,'popnews':popnews}
    return render(request,"home.html",d)
def about(request):
    c=category.objects.all()
    catfeature=news.objects.all()
    popnews=news.objects.all().order_by('-views')[0:3]
    site=main.objects.all()[0]
    d={'site':site,'cat':c,'news':catfeature,'popnews':popnews}
    return render(request,"about.html",d)
def sitesettings(request):
    if request.method=='POST':
        title=request.POST.get('title')
        fb=request.POST.get('fb')
        insta=request.POST.get('insta')
        twitter=request.POST.get('twitter')
        about=request.POST.get('about')
        if(about==""):
            return redirect('panel')
        else:
           
            
            a=main.objects.all()[0]
            a.title=title
            a.fb=fb
            a.insta=insta
            a.twitter=twitter
            a.about=about
            a.save()
            return redirect('panel')

    return render(request,'back/sitesettings.html')

def news_details(request,which_news):
    c=category.objects.all()
    popnews=news.objects.all().order_by('-views')[0:3]
    catfeature=news.objects.all()
   
    #print(trandingnews.title)
    try:
        v=Trandingpost.objects.get(about=which_news)
        trandingnews=Trandingpost.objects.get(about=which_news)
        v.views=v.views+1
        v.save()
        
    except:
        return redirect('home')
    return render(request,"trandingnews_details.html",{"n":trandingnews,"cat":c,'popnews':popnews,"news":catfeature})


def fullcatnews(request,getnews):
    
    c=category.objects.all()
    catfeature=news.objects.all()
    popnews=news.objects.all().order_by('-views')[0:3]
    try:
        v=news.objects.get(about=getnews)
        
        v.views=v.views+1
        v.save()
        n=news.objects.get(about=getnews)
    except:
        return redirect('home')
    #print(trandingnews.title)
    return render(request,"fullcatnews.html",{"n":n,"cat":c,'popnews':popnews,"news":catfeature})
def panel(request):
    if request.user.is_authenticated:
       return render(request,"back/index.html")
    else:
        return redirect(my_login)
    

def news_list(request):
    news=Trandingpost.objects.all()

    return render(request,"back/news_list.html",{"news":news})

def news_add(request):
    if request.method=='POST':
        newstitle=request.POST.get('newstitle')
       
        writer=request.POST.get('writer')
        newsdetails=request.POST.get('newsdetails')
        pubdate=request.POST.get('pub_date')
        
        #print(newstitle,newscat,writer,newsdetails)
        if newstitle=="" or writer=="" or newsdetails=="" or pubdate=="":
            error="All feilds are required"
            return render(request,"back/error.html",{'error':error})
        try:#to check file is uploaded or not
            image=request.FILES['image']
            f=FileSystemStorage()
            filename=f.save(image.name,image)#set name of image and if already present set some random name
            #url=f.url(filename)#make urls for media folder
            if str(image.content_type).startswith("image"):#to check the type of file uploaded
                if image.size<5000000:#to check the size of image uploaded
                    n=Trandingpost(about=newstitle,img=image,title=newstitle,imgname=filename,pub_date=pubdate,details=newsdetails,writer=writer,views=0)
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
    
    
    return render(request,"back/newsadd.html")


def news_delete(request,pk):
    
    news=Trandingpost.objects.get(pk=pk)
    fs=FileSystemStorage()
    fs.delete(news.imgname)
    news.delete()
    
   
    return redirect(news_list)

def my_login(request):
    if request.method=='POST':
        u=request.POST.get('username')
        p=request.POST.get('password')
        if u!="" or p!="":
            user=authenticate(username=u,password=p)
            if user is not None:
                login(request,user)
                return redirect('panel') 
    return render(request,"back/login.html")

def my_logout(request):
    logout(request)
    return redirect(my_login)


