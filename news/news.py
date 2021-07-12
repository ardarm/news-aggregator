from django.conf import settings
from newsapi import NewsApiClient


def get_news(search, page):
    newsapi = NewsApiClient(api_key=settings.APIKEY)

    if search is None or search == "top":
        data = newsapi.get_top_headlines(country='us', page=page)
    else:
        data = newsapi.get_everything(q=search,
                                      sort_by="popularity",
                                      page=page)

    return data


def get_context(data, search):
    REPLACEMENT_IMAGE = "https://www.matthewmurray.com.au/wp-content/uploads/2012/02/whyyoursmartphone.jpg"

    articles = data["articles"]

    context = {"success": True, "data": [], "search": search}

    for article in articles:
        context["data"].append({
            "title":
            article["title"],
            "description":
            article["description"],
            "url":
            article["url"],
            "image":
            REPLACEMENT_IMAGE
            if article["urlToImage"] is None else article["urlToImage"],
            "publishedAt":
            article["publishedAt"]
        })

    return context
