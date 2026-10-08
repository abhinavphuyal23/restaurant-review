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
