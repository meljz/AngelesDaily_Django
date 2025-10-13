from django.shortcuts import get_object_or_404, render
from newsapp.models import Articles


# Create your views here.
def Articles_detail(request, pk):
    articles = get_object_or_404 (Articles, pk=pk)
    context = {
        'articles': articles
    }
    return render (request, "Articles_details.html", context)

def news_list(request):
    articles = Articles.objects.all().order_by('-created_at')
    return render(request, 'news_list.html', {'articles': articles})