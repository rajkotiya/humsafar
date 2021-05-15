from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import ride
from datetime import date
from datetime import datetime
def creatride(request):
    if request.method == 'POST':
        location_i = request.POST['location']
        location_i = location_i.lower()
        destination_i = request.POST['destination']
        destination_i =  destination_i.lower()
        nop_i = request.POST['nop']
        avgspeed_i  = request.POST['avgspeed']
        DATE = request.POST['date']
        acnonac =request.POST.get('AC')
        money = request.POST.get('money')
        print(acnonac)
        # print(DATE)
        print(type(DATE))

        print(date.today())
        date_mask = "%Y-%m-%d"
        date_i = datetime.strptime(DATE,date_mask)
        # date_i = datetime.strftime(date_i,date_mask)
        if request.user.is_authenticated:
            if len(location_i) == 0 or len(destination_i) == 0:
                messages.info(request, 'Please enter valid ')
                return render(request, 'serchride.html')

            if datetime.today() < date_i:
                Ride = ride(user = request.user,location = location_i,destination = destination_i, nop = nop_i,avgspeed = avgspeed_i, date = date_i)
                Ride.save()
                print("ride created")
                return render(request,'home.html')
            else:
                messages.info(request, 'Please enter future or present date')
                return render(request, 'creatride.html')

        else:
            messages.info(request, 'Please login to creat ride')
            return redirect('authentication/login')
       
    else:
        return render(request, 'creatride.html')

def deleteone(request,cid):
    ride.objects.get(pk=cid).delete()
    return redirect('profilepage')

def serchride(request):
    if request.method == 'POST':
        location_i = request.POST['location']
        location_i = location_i.lower()
        print(location_i)
        destination_i = request.POST['destination']
        DATE = request.POST['date']
        destination_i = destination_i.lower()
        if len(location_i) == 0 or len(destination_i) == 0 or len(DATE) == 0:
            messages.info(request, 'Please enter valid ')
            return render(request, 'serchride.html')

        # print(destination_i)
        # print(DATE)
        # print(date.today())
        date_mask = "%Y-%m-%d"
        date_i = datetime.strptime(DATE,date_mask)
        # date_i = datetime.strftime(date_i,date_mask)
        # print(date_i)
        if request.user.is_authenticated:
            rides1 = ride.objects.all().filter(location = location_i)
            rides = rides1.filter(destination = destination_i)
            if datetime.today() < date_i:
                rides = rides.filter(date = date_i)
                data = { 'rides': rides}
                return render(request, 'serchresult.html', data)
            else:
                messages.info(request, 'Please enter future or present date')
                return render(request, 'serchride.html')
            # print(rides.count())
           
        else:
            messages.info(request, 'Please login to creat ride')
            return render('authentication/login')
        
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

