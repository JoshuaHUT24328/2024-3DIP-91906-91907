# Date: 24/07/2024
# Author: Joshua Hutchings
# Version: 1
# Purpose: Create a program that allows the user to book a plane flight

from datetime import datetime

# List of all flights the user can choose from
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

# Constants to be used when accessing the data of flights, so as to improve code readability
FLIGHT_AIRLINE           = 0
FLIGHT_CODE              = 1
FLIGHT_DEST              = 2
FLIGHT_DEST_AIRPORT      = 3
FLIGHT_DEST_AIRPORT_CODE = 4
FLIGHT_DEPT              = 5
FLIGHT_BASE_PRICE        = 6

# Constants which store the age boundaries for tickets
MAX_CHILD_AGE = 17
MAX_ADULT_AGE = 64
MAX_SENIOR_AGE = 125

# Constants to be used when calculating the ticket prices for different age groups
CHILD_TICKET_PRICE = 0.75
ADULT_TICKET_PRICE = 1.00       # No discounts for Adults
SENIOR_TICKET_PRICE = 0.60

# Characters that are not in the alphabet, but that are allowed in a user's name
ACCEPTED_SPECIAL_CHARACTERS = ["-", ".", " ", "'"]

class Flight:
    def __init__(self, airline, flight_code, destination, destination_airport, destination_airport_code, estimated_departure, base_price):
        '''Class Constructor method'''
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

        # Output a string containing all of the information about a flight, spaced out carefully to align with a table.
        print(f"{self.airline: <18} | {self.flight_code: <5} | {self.destination: <38} | {str(self.estimated_departure): <19} | ${self.base_price:.2f}")

    def book_flight(self):
        '''Book the flight for the user'''
        
        # Becomes false once the user has booked a flight, used to help with validating input
        user_booking_flight = True
        while user_booking_flight:
            try:
                # While the user is booking a flight, take their input for the age of whoever will have the ticket.
                # As the user may be booking a flight for more people than just themselves, they are prompted to enter
                # an age every time they book a ticket, rather than just at the beginning of the program.
                user_age = int(input("How old is the recipient of this ticket?: "))

            except:
                print("Please enter an age.")
            else:
                # Validate the user's input and/or determine the age type of the ticket holder.
                if user_age < 0:
                    # Accept 0 as an age because a baby who is just born technically has an age equivalent of 0 years old.
                    print("An age cannot be a negative number, please enter a real age.")
                elif user_age <= MAX_CHILD_AGE:
                    # If the age entered is not less than 0, we already know that it must be greater than or equal to zero,
                    # so we just need to check that it is less than or equal to MAX_CHILD_AGE. That is, we do not need to
                    # do: user_age >= 0 and user_age <= MAX_CHILD_AGE
                    # Instead, for more succint code, we just need to test on the upper limit that user_age <= MAX_CHILD_AGE.
                    age_type = "Child"
                    # As the user has provided input for a valid age type, set user_booking_flight to False to skip any further
                    # iterations of the while loop.
                    user_booking_flight = False
                elif user_age <= MAX_ADULT_AGE:
                    age_type = "Adult"
                    user_booking_flight = False
                elif user_age <= MAX_SENIOR_AGE:
                    age_type = "Senior"
                    user_booking_flight = False
                else:
                    # If the user enters an age which is greater than the maximum senior age (i.e. an age that is 
                    # unrealistically high), tell them to enter a real age and reject their input.
                    print("Please enter a real age.")

        # Once execution reaches this point, the user has provided a valid age type. Thus, instantiate
        # a ticket object for the ticket chosen by the user.
        return Ticket(self.airline, self.flight_code, self.destination, self.destination_airport, self.destination_airport_code, self.estimated_departure, age_type, self.base_price)

class Ticket:
    def __init__(self, airline, flight_code, destination, destination_airport, destination_airport_code, estimated_departure, age_type, base_price):
        self.airline = airline
        self.flight_code = flight_code
        self.destination = destination
        self.destination_airport = destination_airport
        self.destination_airport_code = destination_airport_code
        self.estimated_departure = estimated_departure
        self.age_type = age_type

        self.price = self.calculate_price(base_price)

    def calculate_price(self, base_price):
        '''Calculate price on ticket from base price for flight, as well as other factors'''

        # Start by setting the price as the base price for the flight
        price = base_price
        # Adjust price based on age
        if self.age_type == "Child":
            price *= CHILD_TICKET_PRICE
        elif self.age_type == "Adult":
            price *= ADULT_TICKET_PRICE
        else:
            price *= SENIOR_TICKET_PRICE

        return price

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.tickets = []

    def add_ticket(self, ticket):
        '''Add a ticket that the user has purchased'''
        self.tickets.append(ticket)

    def remove_ticket(self, ticket_number):
        '''Remove a selected ticket that the user purchased'''
        self.tickets.pop(ticket_number)

    def calculate_total_price(self):
        '''Calculate the total price of all the user's tickets'''

        # Variable used to calculate price
        total = 0
        # Iterate through each ticket the user has an increment the total variable by
        # the price of each ticket.
        for ticket in self.tickets:
            total += ticket.price

        return total
    
    def display_tickets(self):
        '''Return a string to display all of the user's tickets'''
        # First checks that the customer's order is not empty before trying to display it
        if len(self.tickets) == 0:
            return "You currently have no tickets"
        else:
            # String to store the output showing information about a ticket
            output_str = f"Summary of tickets ordered by {self.name} ({self.email})\n"
            output_str += "-----------------------------------------------------------------------------------------------------------------\n"

            # Create column headings
            output_str += "#  | Airline            | Code  | Destination                            | Type   | Date/Time           | Price \n"
            output_str += "---|--------------------|-------|----------------------------------------|--------|---------------------|--------\n"
            
            for user_ticket in self.tickets:
                # Display each ticket in the user's order
                output_str += (f"{self.tickets.index(user_ticket) + 1: <2} | {user_ticket.airline: <18} | {user_ticket.flight_code: <5} | {user_ticket.destination_airport: <38} | {str(user_ticket.age_type): <6} | {str(user_ticket.estimated_departure): <19} | ${user_ticket.price:.2f}\n")

            output_str += "-----------------------------------------------------------------------------------------------------------------\n"

            # Display the total price of the user's order
            output_str += f"Total: ${self.calculate_total_price():.2f}"

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

            # Check that the user's name does not contain any invalid characters, and if it does,
            # then make the loop repeat so that the user's input is taken again.
            for character in user_name:
                if character.isalpha() or character in ACCEPTED_SPECIAL_CHARACTERS:
                    continue
                else:
                    print("Your name contains non-alphabetic characters that are not accepted. Please enter a valid name.")
                    user_entered_valid_name = False
                    break

    # Get user input for the user's email
    while not user_entered_valid_email:
        try:
            user_email = input("What is your email?: ")
        except:
            print("Please enter your email.")
        else:
            # Iterate through each character in user's email address to check that there exists an '@'
            # symbol. Given that alphanumeric characters such as numbers, symbols, etc, are allowed in an email
            # address, characters that are not allowed in a name, it becomes more difficult to validate user input
            # for email addresses. However, ALL email addresses must have an @ symbol, so an email address that
            # does not must be invalid.
            for character in user_email:
                if character == '@':
                    user_entered_valid_email = True
                    break

            if user_entered_valid_email == False:
                print("Please enter a valid email address.")

    # Instantiate user object from the user's name and email address which they have provided
    return User(user_name, user_email)

def display_available_flights():
    '''Display a list of flights for the user to book.'''

    # Create column headings
    print("Airline            | Code  | Destination                            | Date/Time           | Price")
    print("-------------------|-------|----------------------------------------|---------------------|---------")

    # Display each flight
    for flight in flights:
        flight.display_flight()

def take_order(user):
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
            print("\nPlease try again\n")
        else:
            # If the customer enters 1, let the customer add a ticket to their order
            if choice == 1:
                # Display flights available for the user to choose from.
                display_available_flights()

                # Becomes true once the user has chosen the flight they want to book,
                # used to help with validation.
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
                            chosen_flight = flight

                    # If the user did not enter a valid flight code, tell them this and make the loop run again.
                    # Otherwise, set user_chosen_flight to True so that they can continue on.
                    if flight_exists == False:
                        print("Please enter the code of a flight on the list!")
                    else:
                        user_chosen_flight = True

                # Instantiate ticket object and add it to the user's order.
                ticket = chosen_flight.book_flight()
                user.add_ticket(ticket)

                # Confirmation for the user to tell them that their ticket has been added to their order.
                print(f"{ticket.age_type}'s Ticket added to order")

            # If the customer enters 2, display the tickets in their order
            elif choice == 2:
                print("")                       # Extra print statement(s) to create newlines for more appealing formatting
                print(user.display_tickets())
                print("")

            # If the customer enters 3, let the customer remove an item from their order
            elif choice == 3:
                # Start by checking that the user has a ticket that can be removed
                if len(user.tickets) != 0:
                    # Display the tickets that the user has
                    print("")
                    print(user.display_tickets())
                    print("")

                    # Becomes true once the user has selected which ticket to remove. Used to help
                    # with validation
                    user_selected_ticket = False
                    # Runs while the user has not yet selected a ticket
                    while not user_selected_ticket:
                        # Take user input for the ticket that the user wants to remove,
                        # uses try/except to validate user input.
                        try:
                            ticket_to_remove = int(input("Enter the number of the ticket you would like to remove: "))
                        except:
                            print("Please enter the number of a ticket you want to remove")
                        else:
                            # Check that the number entered by the user is within a valid range.
                            # If not, the loop will repeat so that the user has another chance to enter
                            # a valid ticket number.
                            if ticket_to_remove > len(user.tickets) or ticket_to_remove <= 0:
                                print("Please enter a number which corresponds to a ticket.")
                            else:
                                user_selected_ticket = True

                    # Remove the selected ticket from the user's order. Note that
                    # ticket_to_remove is 1 greater than the index of the ticket
                    # to be removed, so hence, remove the ticket with an index of
                    # ticket_to_remove - 1, rather than ticket_to_remove.
                    # This is a consequence of the fact that the index of items in
                    # a list start at 0, whereas the number shown next to each ticket
                    # when display starts at 1.
                    user.remove_ticket(ticket_to_remove - 1)
                else:
                    # If the user has no tickets to be removed, tell them this.
                    print("\nYou have no tickets currently so none can be removed.\n")

            # If the customer enters 4, let the customer confirm/finish their order.
            elif choice == 4:
                # Checks if the customer's order is empty. If it is, the customer is not
                # able to confirm it.
                if len(user.tickets) == 0:
                    print("\nYou cannot confirm your order as it is empty.\n")
                else:
                    # Customer is able to confirm/finish their order, so set customer_booking_flights
                    # to False so that the loop while terminate.
                    customer_booking_flights = False

            # If the customer enters 5, let the customer cancel their order and quit the program.
            elif choice == 5:
                # Take user input to ensure that the customer is actually intending on cancelling their order and quitting.
                # Uses try/except and while loop to validate user input.
                user_given_response = False
                while not user_given_response:
                    try:
                        # Take user input
                        user_response = input("\nAre you sure you want to cancel your order and quit (y/n)?: ").strip().lower()
                    except:
                        print("Please enter either y or n.")
                    else:
                        # Respond based on user input
                        if user_response == 'y':
                            # Farewell the user and quit the program
                            print("Have a nice day!")
                            quit()
                        elif user_response == 'n':
                            # Allow while loop to terminate.
                            print("")
                            user_given_response = True
                        else:
                            # Tell the user to enter valid input and allow loop to repeat so that they have another try.
                            print("Please enter either y or n.")

            # If the customer did not enter one of the menu options, tell them they must do so
            else:
                print("\nPlease enter a number which corresponds to one of the options\n")

def confirm_order(user):
    '''Handle the final part of the program where the use can see their finished order and is written to file.'''

    # Display the user's order
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print("---------------------------------------------------------------------------------------------------")
    print(f"{user.display_tickets()}")

    # Write user's ticket information to an external file
    with open("orders.txt", "a") as file:
        file.write(f"\nName: {user.name}\n")
        file.write(f"Email: {user.email}\n")
        file.write(f"{user.display_tickets()}\n")

# List to store each flight as an object
flights = []
# For each flight, instantiate a Flight object for it and add it to the flights list
for flight in ALL_FLIGHTS:
    f = Flight(flight[FLIGHT_AIRLINE], flight[FLIGHT_CODE], flight[FLIGHT_DEST], flight[FLIGHT_DEST_AIRPORT], flight[FLIGHT_DEST_AIRPORT_CODE], flight[FLIGHT_DEPT], flight[FLIGHT_BASE_PRICE])

    flights.append(f)

def main():
    # Greet user and get their information. Use their information
    # to instantiate a User object.
    print("Welcome to the Flight Manager App!")
    user = user_login()

    # Main part of program of taking the user's order.
    take_order(user)

    # If the program reaches this point, the user is happy with their tickets, so display their order and write to file.
    confirm_order(user)

# Used to control loop which calls the main function.
user_using_program = True
while user_using_program:
    # Call main function for program
    main()

    # Take user input for whether wants to use program again, validating it to ensure it is valid.
    user_given_input = False
    while not user_given_input:
        try:
            # Get user input for whether the user wants to use the program again after finishing.
            user_use_again = input("Would you like to make another order (y/n)?: ").strip().lower()
        except:
            print("Please enter either y or n.")
        else:
            if user_use_again == 'y':
                # If user wants to use the program again, stop this while loop running so that the main
                # function is called again.
                user_given_input = True
            elif user_use_again == 'n':
                # If the user wants to quit the program, farewell them and call quit().
                print("Have a good day!")
                quit()
            else:
                # If the user enters invalid input, tell them this and repeat the loop so that their input
                # is taken again.
                print("Please enter either y or n.")