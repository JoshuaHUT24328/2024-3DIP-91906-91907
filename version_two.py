# Date: 31/07/2024
# Author: Joshua Hutchings
# Version: 2
# Purpose: Create a program that allows the user to book a plane flight

from tkinter import *

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


# Setup main window
root = Tk()
root.title("Flight Booking App")
root.geometry("700x400")

def display_size():
    '''Using to determine the size that I want each window to be, will remove when done'''
    print(f"{root.winfo_width()}x{root.winfo_height()}")

def clear_screen():
    """Clear the window to create a 'clean canvas' for a new frame"""

    # Destroy login frame to create a 'clean canvas' for the Main frame.
    login_frame.destroy()

def main_frame():
    '''Main frame of the program'''
    
    # Clear any existing frame from the window before starting to create the main frame
    clear_screen()

    # Main frame
    main_frame = Frame(root)
    main_frame.pack(side = "top", fill = "both", expand = True)

    # Configure the rows and columns to be used in this frame. Doing this manually means that I can
    # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
    # fix the uniformity problem that arises with the grid method.
    main_frame.columnconfigure((0, 2), weight = 2, uniform = 'a')
    main_frame.columnconfigure(1, weight = 3, uniform = 'a')
    main_frame.rowconfigure(0, weight = 2, uniform = 'a')
    main_frame.rowconfigure((1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')

    header_text_lbl = Label(main_frame, text = "Flight Booking App", font = ("Arial", 20))
    header_text_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 3)

    subheader_text_lbl = Label(main_frame, text = "What would you like to do?", font = ("Arial", 12))
    subheader_text_lbl.grid(row = 1, column = 1, sticky = "NEWS")

    book_flight_btn = Button(main_frame, text = "Book Flight")
    book_flight_btn.grid(row = 2, column = 1, sticky = "WE")

    show_tickets_btn = Button(main_frame, text = "Show Tickets")
    show_tickets_btn.grid(row = 3, column = 1, sticky = "WE")
    
    remove_ticket_btn = Button(main_frame, text = "Remove ticket from Order")
    remove_ticket_btn.grid(row = 4, column = 1, sticky = "WE")
    
    finish_order_btn = Button(main_frame, text = "Finish Order")
    finish_order_btn.grid(row = 5, column = 1, sticky = "WE")
    
    cancel_order_btn = Button(main_frame, text = "Cancel Order")
    cancel_order_btn.grid(row = 6, column = 1, sticky = "WE")

def display_available_flights():
    '''Display a list of flights on the screen for the user to book.'''

    clear_screen()
    pass
    """
    # Create column headings
    print("Airline            | Code  | Destination                            | Date/Time           | Price")
    print("-------------------|-------|----------------------------------------|---------------------|---------")

    # Display each flight
    for flight in flights:
        flight.display_flight()
    """

# List to store each flight as an object
flights = []
# For each flight, instantiate a Flight object for it and add it to the flights list
for flight in ALL_FLIGHTS:
    f = Flight(flight[FLIGHT_AIRLINE], flight[FLIGHT_CODE], flight[FLIGHT_DEST], flight[FLIGHT_DEST_AIRPORT], flight[FLIGHT_DEST_AIRPORT_CODE], flight[FLIGHT_DEPT], flight[FLIGHT_BASE_PRICE])

    flights.append(f)

# Login frame
login_frame = Frame(root)
login_frame.pack(side = "top", fill = "both", expand = True)

# Configure the rows and columns to be used in this frame. Doing this manually means that I can
# adjust the relative sizes of each column/row (from setting the weight). It also means that I can
# fix the uniformity problem that arises with the grid method.
login_frame.columnconfigure((0, 2), weight = 2, uniform = 'a')
login_frame.columnconfigure(1, weight = 3, uniform = 'a')
login_frame.rowconfigure(0, weight = 2, uniform = 'a')
login_frame.rowconfigure((1, 2, 3, 4, 5), weight = 1, uniform = 'a')

header_lbl = Label(login_frame, text = "Welcome to the Flight Booking App!", font = ("Arial", 20))
header_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 3)

name_lbl = Label(login_frame, text = "Please enter your name", font = ("Arial", 12))
name_lbl.grid(row = 1, column = 1, sticky = "WENS")

name_entry = Entry(login_frame)
name_entry.grid(row = 2, column = 1, sticky = "WE")

email_lbl = Label(login_frame, text = "Please enter your email", font = ("Arial", 12))
email_lbl.grid(row = 3, column = 1, sticky = "WENS")

email_entry = Entry(login_frame)
email_entry.grid(row = 4, column = 1, sticky = "WE")

email_btn = Button(login_frame, text = "Continue", font = ("Arial", 9), command = main_frame)
email_btn.grid(row = 5, column = 1)

root.mainloop()