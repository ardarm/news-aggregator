from django.shortcuts import render
from django.conf import settings
import request

# Create your views here.
def home(request):
  page = request.GET.get('page', 1)
  search = request.GET.get('search', None)

  if search is None or search == "top":
    url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format("us",1,settings.APIKEY)
  else:
    url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(search,"popularity",page,settings.APIKEY)

  r = request.get(url=url)
  data = r.json

  # continue later

  return render(request, 'index.html', context='')