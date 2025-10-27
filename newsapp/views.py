from django.shortcuts import get_object_or_404, render
from newsapp.models import Articles, Blogs

# articales_details and news_list is both hand to hand
# news_list render news_list then once a bullet is clicked articles_details will render the articles_details.html
def Articles_detail(request, pk):
    articles = get_object_or_404 (Articles, pk=pk)
    context = {
        'articles': articles
    }
    return render (request, "Articles_details.html", context)

def news_list(request):
    articles = Articles.objects.all().order_by('-created_at')
    return render(request, 'news_list.html', {'articles': articles})


# articales_details and news_list is both hand to hand
# news_list render news_list then once a bullet is clicked articles_details will render the articles_details.html
def blog_detail(request, pk):
    blogs = get_object_or_404 (Blogs, pk=pk)
    context = {
        'blogs': blogs
    }
    return render (request, "blog_details.html", context)

def blog_post(request):
    blogs = Blogs.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs': blogs})