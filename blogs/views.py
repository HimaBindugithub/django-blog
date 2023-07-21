from django.shortcuts import get_object_or_404,render,redirect

from . models import Category,Blog

from django.db.models import Q

def posts_by_category(request,category_id):
    #Fetch the posts that belongs to the category with the id category_id
    posts=Blog.objects.filter(status='Published',category=category_id)
    #Use try/except when we want to do some custom action if the category does not exsits
    #if exists it goes to try block ,otherwise it goes to the except block
    
    #try:
    #    category=Category.objects.get(pk=category_id)
    ##    return redirect('home')
    
    #use get_object_or_404 when you want to show error page if the category does not exist
    category=get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        'category':category,

    }
    return render(request,'posts_by_category.html',context)
    



def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status='Published')
    context={
        'single_blog':single_blog,
    }
    return render(request,'blogs.html',context)   

def search(request):
    keyword=request.GET.get('keyword')

    blogs=Blog.objects.filter(Q(title__contains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')
    context={
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request,'search.html',context)