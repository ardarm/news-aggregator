from django.urls import path
from news import views
from .views import SignUpView

urlpatterns = [
    path('', views.home, name="Home"),
    path("search/", views.search, name="Search"),
    path('next', views.load, name="Next"),
    path('signup/', SignUpView.as_view(), name='SignUp'),
    path('showfav', views.show_favourites, name="ShowFav"),
    path('favorite/', views.user_favourite, name='Favourite'),
]
