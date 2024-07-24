# 01/07/2024
# Just for making a (secret) start

from datetime import time

ALL_FLIGHTS = [["Jetstar",           "JQ129", "Hanoi", "Avarua Rarotonga International Airport", "RAR", time(15, 10, 0), 500],
               ["Air New Zealand",   "AB123", "Queenstown", "Airport A",                              "AAA", time(21, 21, 21), 69],
               ["Qantas",            "GG312", "Hanoi", "Airport Z",                              "ZZZ", time(16, 30, 0), 33],
               ["Air New Zesaland",  "AB123", "Christchurch", "Airport AB",                             "AAA", time(21, 21, 21), 69],
               ["Qanstas",           "GG312", "Hanoi", "Airport Z",                              "ZZZ", time(16, 30, 0), 33],
               ["Air Newe Zesaland", "AB123", "New York", "Airport AB",                             "AAA", time(21, 21, 21), 69],
               ["Qanstaks",          "GG312", "Hanoi", "Airport Z",                              "ZZZ", time(16, 30, 0), 33],
               ["Air New Zresaland", "AB123", "Marshall Island", "Airport AB",                             "AAA", time(21, 21, 21), 69],
               ["Qanstaaas",         "GG312", "Hanoi", "Airport Z",                              "ZZZ", time(16, 30, 0), 33]]

FLIGHT_AIRLINE           = 0
FLIGHT_CODE              = 1
FLIGHT_DEST_CITY         = 2
FLIGHT_DEST_AIRPORT      = 3
FLIGHT_DEST_AIRPORT_CODE = 4
FLIGHT_DEPT              = 5
FLIGHT_BASE_PRICE        = 6

class Flight:
    def __init__(self, airline, flight_code, destination_city, destination_airport, estimated_departure, base_price):
        self.airline = airline
        self.flight_code = flight_code
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.estimated_departure = estimated_departure
        self.base_price = base_price                    # Base price is defined as the price for an economy, Adult ticket, with no discounts

    def display_flight(self):
        '''Display flight on list of flights'''

        print(f"{self.airline: <17} | {self.flight_code} | {self.destination_city: <15} | {str(self.estimated_departure): <9} | ${self.base_price:.2f}")

    def book_flight(self):
        '''Book the flight for the user'''
        
        user_booking_flight = True
        while user_booking_flight:
            user_age = int(input("How old is the recipient of this ticket?: "))

            if user_age < 18:
                age_type = "Child"
            elif user_age < 65:
                age_type = "Adult"
            else:
                age_type = "Senior"

            user_booking_flight = False

        return Ticket(self.airline, self.flight_code, self.destination_airport, age_type)

class Ticket:
    def __init__(self, airline, flight_code, destination_airport, age_type):
        self.airline = airline
        self.flight_code = flight_code
        self.destination_airport = destination_airport
        self.age_type = age_type
        self.discount_amount = 0.0

        self.price = self.calculate_price()

    def update_details(self):
        '''Update ticket details'''
        pass

    def calculate_price(self):
        '''Calculate price on ticket from base price for flight, as well as other factors'''
        return 

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.tickets = []

    def add_ticket(self, ticket):
        '''Add a ticket that the user has purchased'''
        self.tickets.append(ticket)

    def remove_ticket(self):
        '''Remove a selected ticket that the user purchased'''
        pass

    def calculate_total_price(self):
        '''Calculate the total price of all the user's tickets'''

        total = 0
        for ticket in self.tickets:
            total += ticket.price

        return total

def user_login():
    '''Get the user's information'''

    # Used to help validate user input
    user_entered_valid_name = False
    user_entered_valid_email = False

    # Get user input for the user's name
    while not user_entered_valid_name:
        try:
            user_name = input("What is your name?: ")
        except:
            print("Please enter your name.")
        else:
            user_entered_valid_name = True

    # Get user input for the user's email
    while not user_entered_valid_email:
        try:
            user_email = input("What is your email?: ")
        except:
            print("Please enter your email.")
        else:
            user_entered_valid_email = True

    # Instantiate user object from their name and email which they have provided
    return User(user_name, user_email)

def display_available_flights():
    '''Display a list of flights for the user to book.'''

    # Create column headings
    print("Airline           | Code  | City            | Date/Time | Price")
    print("------------------|-------|-----------------|-----------|---------")

    # Display each flight
    for flight in flights:
        flight.display_flight()

def loooooop(user):
    """Allows a customer to add/edit/remove/view items in their order."""

    # Is True when the customer is booking their flights. Becomes False
    # when the customer has finished booking their flights.
    customer_booking_flights = True

    # Runs while the customer is booking their flights
    while customer_booking_flights:
        # Gives the user a list of what they can do
        print("""---------------------------------------------------------------------------------------------------
1 - Book flight      3 - Remove ticket from Order      5 - Cancel Order and Quit
2 - Show tickets     4 - Finish Order                  
---------------------------------------------------------------------------------------------------""")

        # Takes user input for what the customer wants to do, uses try/except to validate
        try:
            choice = int(input("Enter the number which corresponds to what you would like to do: ").strip())
        except:
            print("Please try again")
        else:
            # If the customer enters 0, display the menu
            if choice == 0:
                continue

            # If the customer enters 1, let the customer add an item to their order
            elif choice == 1:
                display_available_flights()

                # Becomes true once the user has chosen the flight they want to book,
                # used with validation
                user_chosen_flight = False

                # Take user input for the flight the user wants to book
                while not user_chosen_flight:
                    flight_to_book = input("Enter the code of the flight you want to book: ").strip()

                    # Check that user has entered the code for a flight that exists
                    flight_exists = False

                    # Check the flight code entered by the user with the flight code of each
                    # available flight. This is to make sure that the flight code entered by
                    # the user corresponds to an actual flight that exists.
                    for flight in flights:
                        if flight.flight_code == flight_to_book:
                            flight_exists = True
                            user_flight = flight

                    # If the user did not enter a valid flight code, tell them this.
                    # Otherwise, set user_chosen_flight to True so that they can continue on.
                    if flight_exists == False:
                        print("Please enter the code of a flight on the list!")
                    else:
                        user_chosen_flight = True

                ticket = user_flight.book_flight()
                user.add_ticket(ticket)

                print("Ticket added to order")

            # If the customer enters 2, display the tickets in their order
            elif choice == 2:
                # First checks that the customer's order is not empty before trying to display it
                if len(user.tickets) == 0:
                    print("You currently have no tickets")
                else:
                    for t in user.tickets:
                        
                        # Create column headings
                        print("Airline           | Code  | City            | Date/Time | Type | Price")
                        print("------------------|-------|-----------------|-----------|------|------")

                        # Display each ticket in the user's order
                        print(f"{t.airline: <17} | {t.flight_code} | {t.destination_airport: <15} | {str(t.age_type): <9} | $")

            # If the customer enters 3, let the customer remove an item from their order
            elif choice == 3:
                # Start by checking that the user has a ticket that can be removed
                if len(user.tickets) != 0:
                    # Select what ticket to remove
                    ticket_to_remove = 3

                    user.remove_ticket(ticket_to_remove)
                else:
                    print("You have no tickets currently so none can be removed.")


            # If the customer enters 5, assuming that their order is not blank, set
            # customer_taking_order to False and let them move on to the next stage.
            elif choice == 4:
                # Checks if the customer's order is empty. If it is, the customer is not
                # able to confirm it
                if len(user.tickets) == 0:
                    print("You cannot confirm your order as it is empty.")
                else:
                    customer_booking_flights = False

            # If the customer enters 6, return "Order Cancelled" from the function as they
            # have chosen to cancel their order. This string is used to stop the program
            # later on from trying to add the customer's order to the global list of orders,
            # if the customer has chosen to cancel thier order.
            elif choice == 5:
                user_response = input("Are you sure you want to cancel your order and quit (y/n)?: ").strip().lower()
                if user_response == 'y':
                    print("Have a nice day!")
                    quit()
                elif user_response == 'n':
                    continue
                else:
                    print("Please enter either y or n.")


            # If the customer did not enter one of the menu options, tell them they must do so
            else:
                print("Please enter a number which corresponds to one of the options")


# List to store each flight as an object
flights = []
# For each flight, instantiate a Flight class object for it and add it to the flights list
for flight in ALL_FLIGHTS:
    f = Flight(flight[FLIGHT_AIRLINE], flight[FLIGHT_CODE], flight[FLIGHT_DEST_CITY], flight[FLIGHT_DEST_AIRPORT], flight[FLIGHT_DEPT], flight[FLIGHT_BASE_PRICE])

    flights.append(f)

def main():
    # Greet user and get their information
    print("Welcome to the Flight Manager App!")

    user = user_login()


    #user = User("Joshua", "joshua@gmail.com")
    #ticket = Ticket(test_flight.airline, test_flight.flight_code, test_flight.destination_airport, "Adult")
    #user.add_ticket(ticket)

    loooooop(user)

user_using_program = True
while user_using_program:
    main()

    user_use_again = input("Would you like to make another order (y/n)?: ").strip().lower()
    if user_use_again != 'y':
        user_using_program = False