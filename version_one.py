# Date: 24/07/2024
# Author: Joshua Hutchings
# Version: 1
# Purpose: Create a program that allows the user to book a plane flight

from datetime import datetime

ALL_FLIGHTS = [
    ["Air New Zealand", "NZ101", "Wellington, New Zealand", "Wellington International Airport", "WLG", datetime(2024, 7, 10, 6, 30), 150.0],
    ["Qantas", "QF122", "Sydney, Australia", "Sydney Kingsford Smith Airport", "SYD", datetime(2024, 7, 10, 7, 45), 350.0],
    ["Jetstar", "JQ201", "Melbourne, Australia", "Melbourne Airport", "MEL", datetime(2024, 7, 10, 8, 15), 300.0],
    ["Singapore Airlines", "SQ286", "Singapore, Singapore", "Changi Airport", "SIN", datetime(2024, 7, 10, 9, 00), 750.0],
    ["Cathay Pacific", "CX198", "Hong Kong, Hong Kong", "Hong Kong International Airport", "HKG", datetime(2024, 7, 10, 9, 45), 650.0],
    ["Emirates", "EK407", "Dubai, UAE", "Dubai International Airport", "DXB", datetime(2024, 7, 10, 10, 30), 1200.0],
    ["Virgin Australia", "VA144", "Brisbane, Australia", "Brisbane Airport", "BNE", datetime(2024, 7, 10, 11, 00), 320.0],
    ["Fiji Airways", "FJ410", "Nadi, Fiji", "Nadi International Airport", "NAN", datetime(2024, 7, 10, 11, 45), 400.0],
    ["LATAM Airlines", "LA800", "Santiago, Chile", "Arturo Merino Benítez Airport", "SCL", datetime(2024, 7, 10, 12, 30), 1300.0],
    ["Air Tahiti Nui", "TN102", "Papeete, French Polynesia", "Faa'a International Airport", "PPT", datetime(2024, 7, 10, 13, 15), 900.0],
    ["Qantas", "QF156", "Adelaide, Australia", "Adelaide Airport", "ADL", datetime(2024, 7, 10, 14, 00), 340.0],
    ["Air New Zealand", "NZ105", "Christchurch, New Zealand", "Christchurch International Airport", "CHC", datetime(2024, 7, 10, 14, 45), 160.0],
    ["Malaysia Airlines", "MH130", "Kuala Lumpur, Malaysia", "Kuala Lumpur International Airport", "KUL", datetime(2024, 7, 10, 15, 30), 720.0],
    ["American Airlines", "AA83", "Los Angeles, USA", "Los Angeles International Airport", "LAX", datetime(2024, 7, 10, 16, 15), 1100.0],
    ["United Airlines", "UA916", "San Francisco, USA", "San Francisco International Airport", "SFO", datetime(2024, 7, 10, 17, 00), 1150.0],
    ["Air Canada", "AC34", "Vancouver, Canada", "Vancouver International Airport", "YVR", datetime(2024, 7, 10, 17, 45), 1050.0],
    ["British Airways", "BA16", "London, UK", "Heathrow Airport", "LHR", datetime(2024, 7, 10, 18, 30), 1400.0],
    ["Lufthansa", "LH791", "Frankfurt, Germany", "Frankfurt Airport", "FRA", datetime(2024, 7, 10, 19, 15), 1350.0],
    ["Qatar Airways", "QR921", "Doha, Qatar", "Hamad International Airport", "DOH", datetime(2024, 7, 10, 20, 00), 1250.0],
    ["Japan Airlines", "JL786", "Tokyo, Japan", "Narita International Airport", "NRT", datetime(2024, 7, 10, 20, 45), 980.0],
    ["Korean Air", "KE130", "Seoul, South Korea", "Incheon International Airport", "ICN", datetime(2024, 7, 10, 21, 30), 940.0],
    ["Thai Airways", "TG492", "Bangkok, Thailand", "Suvarnabhumi Airport", "BKK", datetime(2024, 7, 10, 22, 15), 890.0],
    ["China Southern", "CZ306", "Guangzhou, China", "Guangzhou Baiyun International Airport", "CAN", datetime(2024, 7, 10, 23, 00), 820.0],
    ["Air New Zealand", "NZ289", "Shanghai, China", "Shanghai Pudong International Airport", "PVG", datetime(2024, 7, 10, 23, 45), 840.0],
    ["LATAM Airlines", "LA806", "Lima, Peru", "Jorge Chávez International Airport", "LIM", datetime(2024, 7, 11, 0, 30), 1250.0],
    ["Qantas", "QF164", "Perth, Australia", "Perth Airport", "PER", datetime(2024, 7, 11, 1, 15), 370.0],
    ["Air New Zealand", "NZ102", "Wellington, New Zealand", "Wellington International Airport", "WLG", datetime(2024, 7, 11, 6, 30), 150.0],
    ["Qantas", "QF123", "Sydney, Australia", "Sydney Kingsford Smith Airport", "SYD", datetime(2024, 7, 11, 7, 45), 350.0],
    ["Jetstar", "JQ202", "Melbourne, Australia", "Melbourne Airport", "MEL", datetime(2024, 7, 11, 8, 15), 300.0],
    ["Singapore Airlines", "SQ287", "Singapore, Singapore", "Changi Airport", "SIN", datetime(2024, 7, 11, 9, 00), 750.0],
    ["Cathay Pacific", "CX199", "Hong Kong, Hong Kong", "Hong Kong International Airport", "HKG", datetime(2024, 7, 11, 9, 45), 650.0],
    ["Emirates", "EK408", "Dubai, UAE", "Dubai International Airport", "DXB", datetime(2024, 7, 11, 10, 30), 1200.0],
    ["Virgin Australia", "VA145", "Brisbane, Australia", "Brisbane Airport", "BNE", datetime(2024, 7, 11, 11, 00), 320.0],
    ["Fiji Airways", "FJ411", "Nadi, Fiji", "Nadi International Airport", "NAN", datetime(2024, 7, 11, 11, 45), 400.0],
    ["LATAM Airlines", "LA801", "Santiago, Chile", "Arturo Merino Benítez Airport", "SCL", datetime(2024, 7, 11, 12, 30), 1300.0],
    ["Air Tahiti Nui", "TN103", "Papeete, French Polynesia", "Faa'a International Airport", "PPT", datetime(2024, 7, 11, 13, 15), 900.0],
    ["Qantas", "QF157", "Adelaide, Australia", "Adelaide Airport", "ADL", datetime(2024, 7, 11, 14, 00), 340.0],
    ["Air New Zealand", "NZ106", "Christchurch, New Zealand", "Christchurch International Airport", "CHC", datetime(2024, 7, 11, 14, 45), 160.0],
    ["Malaysia Airlines", "MH131", "Kuala Lumpur, Malaysia", "Kuala Lumpur International Airport", "KUL", datetime(2024, 7, 11, 15, 30), 720.0],
    ["American Airlines", "AA84", "Los Angeles, USA", "Los Angeles International Airport", "LAX", datetime(2024, 7, 11, 16, 15), 1100.0],
    ["United Airlines", "UA917", "San Francisco, USA", "San Francisco International Airport", "SFO", datetime(2024, 7, 11, 17, 00), 1150.0],
    ["Air Canada", "AC35", "Vancouver, Canada", "Vancouver International Airport", "YVR", datetime(2024, 7, 11, 17, 45), 1050.0],
    ["British Airways", "BA17", "London, UK", "Heathrow Airport", "LHR", datetime(2024, 7, 11, 18, 30), 1400.0],
    ["Lufthansa", "LH792", "Frankfurt, Germany", "Frankfurt Airport", "FRA", datetime(2024, 7, 11, 19, 15), 1350.0],
    ["Qatar Airways", "QR922", "Doha, Qatar", "Hamad International Airport", "DOH", datetime(2024, 7, 11, 20, 00), 1250.0],
    ["Japan Airlines", "JL787", "Tokyo, Japan", "Narita International Airport", "NRT", datetime(2024, 7, 11, 20, 45), 980.0],
    ["Korean Air", "KE131", "Seoul, South Korea", "Incheon International Airport", "ICN", datetime(2024, 7, 11, 21, 30), 940.0],
    ["Thai Airways", "TG493", "Bangkok, Thailand", "Suvarnabhumi Airport", "BKK", datetime(2024, 7, 11, 22, 15), 890.0],
    ["China Southern", "CZ307", "Guangzhou, China", "Guangzhou Baiyun International Airport", "CAN", datetime(2024, 7, 11, 23, 00), 820.0],
    ["Air New Zealand", "NZ290", "Shanghai, China", "Shanghai Pudong International Airport", "PVG", datetime(2024, 7, 11, 23, 45), 840.0],
    ["LATAM Airlines", "LA807", "Lima, Peru", "Jorge Chávez International Airport", "LIM", datetime(2024, 7, 12, 0, 30), 1250.0],
    ["Qantas", "QF165", "Perth, Australia", "Perth Airport", "PER", datetime(2024, 7, 12, 1, 15), 370.0]
    ]

#ALL_FLIGHTS = [["Jetstar",           "JQ129", "Hanoi", "Avarua Rarotonga International Airport", "RAR", time(15, 10, 0), 500],
#               ["Air New Zealand",   "AB123", "Queenstown", "Airport A",                              "AAA", time(21, 21, 21), 69],
#               ["Qantas",            "GG312", "Hanoi", "Airport Z",                              "ZZZ", time(16, 30, 0), 33],
#               ["Air New Zesaland",  "AB123", "Christchurch", "Airport AB",                             "AAA", time(21, 21, 21), 69],
#               ["Qanstas",           "GG312", "Hanoi", "Airport Z",                              "ZZZ", time(16, 30, 0), 33],
#               ["Air Newe Zesaland", "AB123", "New York", "Airport AB",                             "AAA", time(21, 21, 21), 69],
#               ["Qanstaks",          "GG312", "Hanoi", "Airport Z",                              "ZZZ", time(16, 30, 0), 33],
#               ["Air New Zresaland", "AB123", "Marshall Island", "Airport AB",                             "AAA", time(21, 21, 21), 69],
#               ["Qanstaaas",         "GG312", "Hanoi", "Airport Z",                              "ZZZ", time(16, 30, 0), 33],
#               ["Air New Zealand", "NZ990", "Apia, Fiji", "Faleolo International Airport", "APW", time(8, 45, 0), ]]

FLIGHT_AIRLINE           = 0
FLIGHT_CODE              = 1
FLIGHT_DEST              = 2
FLIGHT_DEST_AIRPORT      = 3
FLIGHT_DEST_AIRPORT_CODE = 4
FLIGHT_DEPT              = 5
FLIGHT_BASE_PRICE        = 6

class Flight:
    def __init__(self, airline, flight_code, destination, destination_airport, destination_airport_code, estimated_departure, base_price):
        self.airline = airline
        self.flight_code = flight_code
        self.destination = destination
        self.destination_airport = destination_airport
        self.destination_airport_code = destination_airport_code
        self.estimated_departure = estimated_departure
        self.base_price = base_price                    # Base price is defined as the price for an economy, Adult ticket, with no discounts.
                                                        # For a different type of ticket (first class, child ticket, etc), the price of the ticket will be calculated to account for this.
    def display_flight(self):
        '''Display flight on list of flights'''

        print(f"{self.airline: <18} | {self.flight_code: <5} | {self.destination: <25} | {str(self.estimated_departure): <19} | ${self.base_price:.2f}")

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

        return Ticket(self.airline, self.flight_code, self.destination_airport, age_type, self.base_price)

class Ticket:
    def __init__(self, airline, flight_code, destination_airport, age_type, base_price):
        self.airline = airline
        self.flight_code = flight_code
        self.destination_airport = destination_airport
        self.age_type = age_type
        self.discount_amount = 0.0

        self.price = self.calculate_price(base_price)

    def update_details(self):
        '''Update ticket details'''
        pass

    def calculate_price(self, base_price):
        '''Calculate price on ticket from base price for flight, as well as other factors'''
        return base_price

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
    
    def display_tickets(self):
        '''Return a string to display all of the user's tickets'''
        # First checks that the customer's order is not empty before trying to display it
        if len(self.tickets) == 0:
            print("You currently have no tickets")
        else:
            output_str = ""

            # Create column headings
            output_str += "Airline            | Code  | Destination               | Date/Time           | Type   | Price \n"
            output_str += "-------------------|-------|---------------------------|---------------------|--------|-------\n"
            
            for t in self.tickets: 
                # Display each ticket in the user's order
                output_str += (f"{t.airline: <18} | {t.flight_code: <5} | {t.destination_airport: <25} | {str(t.age_type): <9} | ${t.price}\n")

            return output_str

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
    print("Airline            | Code  | Destination               | Date/Time           | Price")
    print("-------------------|-------|---------------------------|---------------------|---------")

    # Display each flight
    for flight in flights:
        flight.display_flight()

def loooooop(user):
    """Handle the main part of the program where the user is ordering tickets, managing their order, etc."""

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
                print(user.display_tickets())

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

def checkout(user):
    '''Handle the final part of the program where the use can see their finished order and is written to file.'''

    # Display the user's order
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print("-------------------------------------------------------------------------------------")
    user.display_tickets()
    print(f"Total price ${user.calculate_total_price()}")

    with open("orders.txt", "a") as file:
        file.write(f"Name: {user.name}\n")
        file.write(f"Email: {user.email}\n")
        file.write(user.display_tickets())

# List to store each flight as an object
flights = []
# For each flight, instantiate a Flight class object for it and add it to the flights list
for flight in ALL_FLIGHTS:
    f = Flight(flight[FLIGHT_AIRLINE], flight[FLIGHT_CODE], flight[FLIGHT_DEST], flight[FLIGHT_DEST_AIRPORT], flight[FLIGHT_DEST_AIRPORT_CODE], flight[FLIGHT_DEPT], flight[FLIGHT_BASE_PRICE])

    flights.append(f)

def main():
    # Greet user and get their information. Use their information
    # to instantiate a User object.
    print("Welcome to the Flight Manager App!")
    user = user_login()

    loooooop(user)

    # If the program reaches this point, the user is happy with their tickets
    checkout(user)

user_using_program = True
while user_using_program:
    main()

    user_use_again = input("Would you like to make another order (y/n)?: ").strip().lower()
    if user_use_again != 'y':
        user_using_program = False