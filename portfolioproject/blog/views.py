from gc import get_objects
from django.shortcuts import get_object_or_404, render
from .models import Blogmodel

# Create your views here.
def allblogs(requests):
    blogs=Blogmodel.objects.order_by('blogdate')
    return render(requests, 'blog/allblogs.html',{"blogs":blogs})

def detail(requests,blog_id):
    blog=get_object_or_404(Blogmodel,pk=blog_id)
    return render(requests, 'blog/blogdetail.html',{"blog":blog})