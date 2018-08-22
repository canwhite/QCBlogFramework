from django.shortcuts import render
from blog.models import CommonData
from django.http import HttpResponse

def index(request):
    
    return render(request,'index.html')   # 返回index.html

# Create your views here.
def aboutus(request):
    
    return render(request,'about.html')   # 返回index.html

def gbook(request):
    
    return render(request,'gbook.html')

def info(request):
    
    return render(request,'info.html')

def infopic(request):
    
    return render(request,'infopic.html')

def list(request):
    
    return render(request,'list.html')

def share(request):
    
    return render(request,'share.html')

def getdata(request):
    
    return HttpResponse({'<apps><app><id>1</id><name>Google Maps</name><version>1.0</version></app><app><id>2</id><name>Chrome</name><version>2.1</version></app><app><id>3</id><name>Chrome Play</name><version>2.3</version></app></apps>'},content_type = "text/xml")
    
