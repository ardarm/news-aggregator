from django.urls import path
from news import views
from .views import SignUpView

urlpatterns = [
    path('', views.home, name="Home"),
    path("search/", views.search, name="Search"),
    path('next', views.load, name="Next"),
    path('signup/', SignUpView.as_view(), name='SignUp'),
    path('bookmark/', views.user_bookmark, name='user_bookmark'),
    path('showfav', views.show_favourites, name="ShowFav"),
]
