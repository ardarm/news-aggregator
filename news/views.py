from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from news import get_news


# Create your views here.
def home(request):
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    data = get_news(search, page)

    if not data["status"] == "ok":
        return HttpResponse("<h1>Request Failed</h1>")

    context = {
        "success": True,
        "data": [],
        "search": search
    }

    articles = data["articles"]

    for article in articles:
        context["data"].append(
            {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "image": article["urlToImage"],
                "publishedAt": article["publishedAt"]
            }
        )

    return render(request, 'index.html', context=context)
