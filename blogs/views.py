from django.shortcuts import get_object_or_404,render,redirect

from . models import Category,Blog

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