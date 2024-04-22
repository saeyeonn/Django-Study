class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passsenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)


capacity = 500
flight = Flight(capacity)

print(flight.capacity)

people = ['Saeyeon', 'Cherry', 'Pochacco']

for person in people:
    if flight.add_passsenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")

open_seats = flight.open_seats()

print(open_seats)