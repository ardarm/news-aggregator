from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from news.news import get_news

replacement_image = "https://www.matthewmurray.com.au/wp-content/uploads/2012/02/whyyoursmartphone.jpg"


# Create your views here.
def home(request):
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    data = get_news(search, page)

    if not data["status"] == "ok":
        return HttpResponse("<h1>Request Failed</h1>")

    context = {"success": True, "data": [], "search": search}

    articles = data["articles"]

    for article in articles:
        context["data"].append({
            "title":
            article["title"],
            "description":
            article["description"],
            "url":
            article["url"],
            "image":
            replacement_image
            if article["urlToImage"] is None else article["urlToImage"],
            "publishedAt":
            article["publishedAt"]
        })

    return render(request, 'index.html', context=context)


def search(request):
    if request.method == "POST":
        page = request.GET.get('page', 1)
        keyword = request.POST.get("keyword")

        data = get_news(keyword, page)

        if not data["status"] == "ok":
            return HttpResponse("<h1>Request Failed</h1>")

        context = {"success": True, "data": [], "search": keyword}

        articles = data["articles"]

        for article in articles:
            context["data"].append({
                "title":
                article["title"],
                "description":
                article["description"],
                "url":
                article["url"],
                "image":
                replacement_image
                if article["urlToImage"] is None else article["urlToImage"],
                "publishedAt":
                article["publishedAt"]
            })

        return render(request, 'index.html', context=context)

    else:

        return render(request, 'index.html')
