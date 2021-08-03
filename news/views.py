from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

from news.news import get_news, get_context
from news.models import UserArticle

REPLACEMENT_IMAGE = "https://www.matthewmurray.com.au/wp-content/uploads/2012/02/whyyoursmartphone.jpg"


# Create your views here.
def home(request):
    user = request.user
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    data = get_news(search, page)

    if not data["status"] == "ok":
        return HttpResponse("<h1>Request Failed</h1>")

    context = get_context(data, search)

    if user.is_authenticated:
        user_favorites = {
            ua.url for ua in
            UserArticle.objects.filter(user=user)
        }
    else:
        user_favorites = set()
    context["user_favorites"] = user_favorites

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


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@ login_required
def show_favourites(request):
    return render(request, 'favourites.html')


@ login_required
def user_bookmark(request):
    user = request.user
    url = request.GET["article"]
    checked = request.GET.get('checked', False)
    user_article, created = UserArticle.objects.get_or_create(
        user=user,
        url=url)
    # if bookmark was checked it was bookmarked, now I want to remove
    # the bookmark
    if checked:
        user_article.delete()
    return JsonResponse({"status": "success"})
