from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    breaking=bnews.objects.all().order_by('-id')[0:10]
    slinews=hnews.objects.all().order_by('-id')[0:5]
    cdata=category.objects.all().order_by('-id')[0:6]
    ncdata=newcategory.objects.all().order_by('-id')[0:12]
    trendi=trending.objects.all().order_by('-id')[0:6]
    return render(request,'user/index.html',{"slide":slinews,"data":cdata,"cdata":ncdata,"trend":trendi,"brnews":breaking})

def about(request):
    breaking = bnews.objects.all().order_by('-id')[0:10]
    return render(request,'user/about.html',{'brnews':breaking})

def contactus(request):
    breaking = bnews.objects.all().order_by('-id')[0:10]
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Email=request.POST.get("email","")
        Mobile=request.POST.get("mobile","")
        Message=request.POST.get("msg","")
        res=contact(name=Name,email=Email,mobile=Mobile,message=Message)
        res.save()
        status=True

    return render(request,'user/contactus.html',{'S':status,"brnews":breaking})

def login(request):
    if request.method=='POST':
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        mobile=request.POST.get("mobile","")
        password=request.POST.get("passwd","")
        address=request.POST.get("address","")
        picname=request.FILES["fu"]
        profile(name=name,mobile=mobile,email=email,passwd=password,address=address,ppick=picname).save()
        return HttpResponse("<script>alert('You Are Registered successfully..');window.location.href='/user/login/';</script>")

    return render(request,'user/login.html')

def video(request):
    breaking = bnews.objects.all().order_by('-id')[0:10]
    vide=videos.objects.all().order_by('-id')
    return render(request,'user/videos.html',{"vid":vide,"brnews":breaking})

def viewnews(request):
    breaking = bnews.objects.all().order_by('-id')[0:10]
    ndata=news.objects.all().order_by('-id')[0:6]
    tndata=tnews.objects.all().order_by('-id')[0:2]
    tsdata=tsnews.objects.all().order_by('-id')[0:10]
    return render(request,'user/viewnews.html',{"news":ndata,"tnews":tndata,"tsnews":tsdata,"brnews":breaking})

def viewmore(request):
    breaking = bnews.objects.all().order_by('-id')[0:10]
    a=request.GET.get('msg')
    b=request.GET.get('xyz')
    c=request.GET.get('abc')
    d=request.GET.get('tren')
    e=request.GET.get('ayz')
    f=request.GET.get('a')
    g=request.GET.get('b')
    h=request.GET.get('c')
    i=request.GET.get('d')
    j=request.GET.get('e')
    k=request.GET.get('sli')
    l=request.GET.get('vid')
    ndata=news.objects.filter(id=a)
    tndata=tnews.objects.filter(id=b)
    tsdata=tsnews.objects.filter(id=c)
    trend=trending.objects.filter(id=d)
    breaki=bnews.objects.filter(id=e)
    fcat=newcategory.objects.filter(id=f)
    scat=newcategory.objects.filter(id=g)
    tcat=newcategory.objects.filter(id=h)
    focat=newcategory.objects.filter(id=i)
    ficat=newcategory.objects.filter(id=j)
    hn=hnews.objects.filter(id=k)
    vi=videos.objects.filter(id=l)
    return render(request,'user/viewmore.html',{"data":ndata,"tdata":tndata,"trdata":tsdata,"tren":trend,"bne":breaki,'fc':fcat,'sc':scat,'tc':tcat,'foc':focat,'fic':ficat,'hnew':hn,"brnews":breaking,'vid':vi})

def vnews(request):
    breaking = bnews.objects.all().order_by('-id')[0:10]
    cdata=category.objects.all().order_by('-id')

    a=request.GET.get('abc')
    ndata=""
    if a is None:
        ndata = news.objects.all().order_by('-id')
    else:
        ndata=news.objects.filter(ncategory=a)


    return render(request,'user/news.html',{"c":cdata,"n":ndata,"brnews":breaking})