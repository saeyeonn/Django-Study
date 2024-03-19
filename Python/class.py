class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name}")

saeyeon = Person("Saeyeon", 29)
saeyeon.greet()

cherry = Person("Cherry", 5)
cherry.greet()




class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def set_passsenger(self, name):
        self.passengers.append(name)
    def open_seats(self):
        return self.capacity - len(self.passengers)


capacity = 500
itm_flight = Flight(capacity)
print(itm_flight.capacity)

people = ['Saeyeon', 'Cherry', 'Pochacco']

for person in people:
    itm_flight.set_passsenger(person)

open_seats = itm_flight.open_seats()
print(open_seats)
