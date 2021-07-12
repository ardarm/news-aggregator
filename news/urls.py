from django.urls import path
from news import views

urlpatterns = [
    path('', views.home, name="Home"),
    path("search/", views.search, name="Search"),
    path('next', views.load, name="Next"),
]
