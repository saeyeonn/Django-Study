from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "users/login.html")
    # return render(request, "flights/index.html", {
    #     "flights" : Flight.objects.all()
    # })
    
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passenger = Passenger.objects.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passenger": passenger,
        "non_passengers": non_passengers
    })
    
def book(request, flight_id):
    if request.method == "POST":
        
        flight = Flight.objects.get(flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk = passenger_id)
        passenger.flights.add(flight)
        
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
    
