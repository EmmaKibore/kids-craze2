from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):

    return render(request, 'home.html')

def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    return render(request, 'profile.html', {"profile":profile}) 

def search_results(request):
    if 'term' in request.GET and request.GET["term"]:
        search_term = request.GET.get("term")
        searched_term = term.objects.filter(name=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )
      
        return render(request, 'search.html',{"message":message,"term": searched_term,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def categories(request):
    categories = Category.objects.filter()
    images = Image.objects.all()[:5]
    shoes = Image.objects.filter(category__image_category='shoes')[:1]
    cloths = Image.objects.filter(category__image_category='cloths').first()
    accessories = Image.objects.filter(category__image_category='accessories').first()

    return render(request,'categories.html',{"categories":categories, "images":images,"shoes":shoes,"cloths":cloths,"accessories":accessories}) 

def category(request,id):
    categories = Category.objects.all()
    images = Image.objects.filter(category=id)
    return render(request, 'category.html',{ "images":images})    





