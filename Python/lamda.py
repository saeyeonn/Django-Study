square = lambda x: x * x

people = [
    {"name": "Saeyeon", "house": "Seoul"},
    {"name": "Cherry", "house": "York"},
    {"name": "Pochacco", "house": "Toyko"}
]

# way 1
def f(person):
    return person["name"]

people.sort(key=f)

# way 2
people.sort(key=lambda person: person["name"])

print(people)