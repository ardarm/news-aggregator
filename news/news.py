from django.conf import settings
from newsapi import NewsApiClient


def get_news(search, page):
    newsapi = NewsApiClient(api_key=settings.APIKEY)

    if search is None or search == "top":
        data = newsapi.get_top_headlines(country='us', page=1)
    else:
        data = newsapi.get_everything(q=search,
                                      sort_by="popularity",
                                      page=page)

    return data
