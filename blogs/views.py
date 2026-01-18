from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id ):
    #fetch the posts that belongs to the category id

    posts= Blog.objects.filter(status='Published', category=category_id)
    # try except block if some category doen not exist
    #try:
    #    category = Category.objects.get(pk=category_id)
    #except:
        # redirect the user to the homepage if certain category does not exist
    #    return redirect('home')
    
    # Use get_object_or_404 when you want to show just the 404 error page
    category = get_object_or_404(Category, pk=category_id)

    context={
        'posts':posts,
        'category': category,
    }

    return render(request, 'posts_by_category.html', context)