class Artwork:
    """Artwork class"""
    def __init__(self, title, artist, dateOfCreation, historicalSignificance):
        # Initializing the attributes
        self.title = title
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance

    def __str__(self):
        return f"Artwork: {self.title} by {self.artist}, created on {self.dateOfCreation}, significance: {self.historicalSignificance}"
    # Getters and Setters
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_dateOfCreation(self):
        return self.dateOfCreation

    def set_dateOfCreation(self, dateOfCreation):
        self.dateOfCreation = dateOfCreation

    def get_historicalSignificance(self):
        return self.historicalSignificance

    def set_historicalSignificance(self, historicalSignificance):
        self.historicalSignificance = historicalSignificance
class Exhibition:
    def __init__(self, title, location, duration):
        self.title = title
        self.location = location
        self.duration = duration
        self.artworks = []

    def __str__(self):
        return f"Exhibition: {self.title}, Location: {self.location.name}, Duration: {self.duration} days"

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def remove_artwork(self, artwork):
        self.artworks.remove(artwork)


class Location:
    def __init__(self, name, location_type):
        self.name = name
        self.location_type = location_type

    def __str__(self):
        return f"Location: {self.name}, Type: {self.location_type}"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_location_type(self):
        return self.location_type

    def set_location_type(self, location_type):
        self.location_type = location_type


class Visitor:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.ticket = None

    def __str__(self):
        return f"Visitor: {self.name}, Age: {self.age}, ID: {self.id}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_ticket(self):
        return self.ticket

    def set_ticket(self, ticket):
        self.ticket = ticket

    def buy_ticket(self, ticket):
        self.ticket = ticket


class Ticket:
    def __init__(self, type, price, event, visitor):
        self.type = type
        self.price = price
        self.event = event
        self.visitor = visitor

    def __str__(self):
        return f"Ticket Type: {self.type}, Price: {self.price}, Event: {self.event.title}, Visitor: {self.visitor.name}"

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_event(self):
        return self.event

    def set_event(self, event):
        self.event = event

    def get_visitor(self):
        return self.visitor

    def set_visitor(self, visitor):
        self.visitor = visitor

    def calculate_price(self):
        return self.price * 1.05
    # printing the receipt
    def print_receipt(self):
        print("Receipt:")
        print(f"Ticket Type: {self.type}")
        print(f"Price: {self.calculate_price()}")
        print(f"Event: {self.event.title}")
        print(f"Visitor: {self.visitor.name}")


class Event:
    def __init__(self, title, location, duration, price):
        self.title = title
        self.location = location
        self.duration = duration
        self.price = price

    def __str__(self):
        return f"Event: {self.title}, Location: {self.location.name}, Duration: {self.duration} days, Price: {self.price}"

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
