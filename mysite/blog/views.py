from django.shortcuts import render
from blog.models import BlogsPost

def index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
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

        
    