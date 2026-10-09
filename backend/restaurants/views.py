from django.shortcuts import render

# Create your views here.


from .models import Restaurant

def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    return render(request,'restaurants/restaurant.html',{
        'restaurants':restaurants
    })
    
def index(request):
    restaurants = Restaurant.objects.all()

    return render(request,'restaurants/index.html',{
        'restaurants':restaurants
    })

def login(request):
    restaurants = Restaurant.objects.all()

    return render(request,'restaurants/login.html',{
        'restaurants':restaurants
    })

def signup(request):
    restaurants = Restaurant.objects.all()

    return render(request,'restaurants/signup.html',{
        'restaurants':restaurants
    })

def restaurant_detail(request):
    restaurants = Restaurant.objects.all()

    return render(request,'restaurants/restaurant-detail.html',{
        'restaurants':restaurants
    })

def userprofile(request):
    restaurants = Restaurant.objects.all()

    return render(request,'restaurants/userprofile.html',{
        'restaurants':restaurants
    })

def writereview(request):
    restaurants = Restaurant.objects.all()

    return render(request,'restaurants/writereview.html',{
        'restaurants':restaurants
    })





