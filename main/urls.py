from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",views.index, name = "index"),
    path("login/",views.login, name = "login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/",views.register, name = "register"),
    path("submit_cart/",views.submit_cart, name = "submit_cart"),
    path("movie/category/<str:name>/", views.MovieCategory, name='movie_category'),
    path("movie/detail/<int:pk>/", views.MovieDetail, name='movie_detail'),
    path("movie/check_availability/<str:movie_name>", views.check_availability, name='check_availability'),

]