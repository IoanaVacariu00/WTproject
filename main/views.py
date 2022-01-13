from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Category, Movie


# Create your views here.

def index(request):
	movies = Movie.objects.all()
	
	return render(request, 'home.html', {'movies': movies})


def v1(response):
	return HttpResponse ("<h1>view 1!</h1>")


def login(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')
			
			user = auth.authenticate(username=username, password=password)
			if user:
				auth.login(request, user)
				return HttpResponseRedirect('/')
			else:
				return render(request, 'sign-in.html', {'message':'Username or password is not correct. Try again'})
		return render(request, 'sign-in.html')

	else:
		return HttpResponseRedirect("/")
	

def register(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			username = request.POST.get('username')
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')

			if password1 != password2:
				return render(request, 'register.html', {'message':'Password and confirm password does not match'})
			
			if len(password1) < 7:
				return render(request, 'register.html', {'message':'Password field cannot be less than 8 characters'})
			
			if User.objects.filter(username=username).exists():
				return render(request, 'register.html', {'message':'Username already exists'})

			user = User.objects.create(username=username)
			user.set_password(password1)
			user.save()
			auth.login(request, user)
			return HttpResponseRedirect("/")
		
		return render(request, 'register.html')
	else:
		return HttpResponseRedirect("/")



def MovieCategory(request, name):
	category = Category.objects.filter(name=name).first()
	movies = Movie.objects.filter(category=category)
	class_active = category.name
	
	return render(request, 'movie-category.html', {'movies':movies, 'active':class_active})


def MovieDetail(request, pk):
	# filter().first() is similar to get()
	# avoid get() as much as possible. it will stop your application if there is a missing information
	movie = Movie.objects.filter(pk=pk).first()
	category = movie.category
	similar_movies = Movie.objects.filter(category=category).exclude(pk=pk)[:4]
	star_checked = range(movie.rating)


	return render(request, 'movie-detail.html', {'movie':movie, 'similar_movies':similar_movies, 'stars':star_checked})


def AddtoCart(request, pk):
	movie = Movie.objects.filter(pk=pk).first()
	movie.available = False
	# user = 

def check_availability(request,movie_name):
	movie = Movie.objects.filter(name=movie_name).first()
	if movie.available:
		return HttpResponse(status=200)
	else:
		return HttpResponse(status=404)
def submit_cart(request):
	if request.method == "POST":
		print(request.POST)
		movies = dict(request.POST)['movies']
		for movie in movies:
			movie = get_object_or_404(Movie,name=movie)
			movie.available = False
			movie.save()
			
		return redirect("index")
