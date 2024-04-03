from EventBooking import *
from datetime import date

if __name__ == "__main__":
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", date(1503, 1, 1), "Iconic portrait")
    exhibition = Exhibition("Masterpieces of Renaissance", Location("Room 101", "Gallery"), 30)
    exhibition.add_artwork(artwork1)
    print(exhibition)

    visitor1 = Visitor("V001", "Khalid", 30)
    ticket = Ticket("Regular", 63, Event("Renaissance Art Exhibition", exhibition.location, 30, 80), visitor1)
    visitor1.buy_ticket(ticket)
    print(visitor1.ticket)
    visitor1.ticket.print_receipt()
