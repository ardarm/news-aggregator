from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from news.news import get_news, get_context

REPLACEMENT_IMAGE = "https://www.matthewmurray.com.au/wp-content/uploads/2012/02/whyyoursmartphone.jpg"


# Create your views here.
def home(request):
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    data = get_news(search, page)

    if not data["status"] == "ok":
        return HttpResponse("<h1>Request Failed</h1>")

    context = get_context(data, search)

    return render(request, 'index.html', context=context)


def search(request):
    if request.method == "POST":
        page = request.GET.get('page', 1)
        keyword = request.POST.get("keyword")

    data = get_news(keyword, page)

    if not data["status"] == "ok":
        return HttpResponse("<h1>Request Failed</h1>")

    context = get_context(data, keyword)

    return render(request, 'index.html', context=context)


def load(request):
    page = int(request.GET.get('page', 1))
    search = request.GET.get('search', None)

    data = get_news(search, page)

    context = get_context(data, search)

    return JsonResponse(context)
