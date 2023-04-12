from flight import Flight
class airline:
    def __init__(self, name, country, code, flights: list, employees):
        self.name = name
        self.country = country
        self.code = code
        self.flights = flights
        self.employees = employees

    def add_flight(self, flight: Flight):
        self.flights.append(flight)
        print(f"{flight} is added to {self} airline!")

    def remove_flight(self, flight: Flight):
        self.flights.remove(flight)
        print(f"{flight} is removed from {self} airline!")

    def get_flights(self):
        return self.flights