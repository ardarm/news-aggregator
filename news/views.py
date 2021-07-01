from django.shortcuts import render
from django.conf import settings
from news import get_news


# Create your views here.
def home(request):
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    data = get_news(search, page)

    # continue later

    return render(request, 'index.html', context='')
