from django.shortcuts import render,get_object_or_404
from .models import Blog,Contact

# Create your views here.
def allblogs(request):
    blog = Blog.objects
    return render(request,'blog/allblogs.html',{'blog':blog})

def detail(request,blog_id):
    blogdetail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blogdetail})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        email = request.POST.get('email','')
        comment = request.POST.get('comment','')
        contact = Contact(first_name=first_name,last_name=lname,email=email,comment=comment)
        contact.save()
    return render(request,'blog/contact.html')

def base(request):
    return render(request,'blog/base.html')
