from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import ride
def creatride(request):
    if request.method == 'POST':
        location_i = request.POST['location']
        location_i = location_i.lower()
        print(location_i)
        destination_i = request.POST['destination']
        destination_i =  destination_i.lower()
        print(destination_i)
        nop_i = request.POST['nop']
        avgspeed_i  = request.POST['avgspeed']
        date_i = request.POST['date'] 
        
        if request.user.is_authenticated:
            Ride = ride(user = request.user,location = location_i,destination = destination_i, nop = nop_i,avgspeed = avgspeed_i, date = date_i)
            Ride.save()
            print("ride created")
            return redirect('/')
        else:
            messages.info(request, 'Please login to creat ride')
            return redirect('authentication/login')
       
    else:
        return render(request, 'creatride.html')

def serchride(request):
    if request.method == 'POST':
        location_i = request.POST['location']
        location_i = location_i.lower()
        print(location_i)
        destination_i = request.POST['destination']
        destination_i = destination_i.lower()
        print(destination_i)
        if request.user.is_authenticated:
            rides1 = ride.objects.all().filter(location = location_i)
            rides = rides1.filter(destination = destination_i)
            data = { 'rides': rides}
           
            print(rides.count())
            return render(request, 'serchresult.html', data)
        else:
            messages.info(request, 'Please login to creat ride')
            return redirect('authentication/login')
    else:
        return render(request, 'serchride.html')


def profilepage(request):
    rides=ride.objects.filter(user = request.user)
    data= {'rides':rides}
    return render(request, 'profilepage.html', data)

def home(request):
    return render(request, 'home.html')


def contactus(request):
    return render(request, 'contactus.html')


def aboutus(request):
    return render(request, 'aboutus.html')

