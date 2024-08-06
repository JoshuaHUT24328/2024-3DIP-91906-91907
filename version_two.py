# Date: 06/08/2024
# Author: Joshua Hutchings
# Version: 2
# Purpose: Create a program that allows the user to book a plane flight

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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

class Ticket:
    def __init__(self, holder_name, airline, flight_code, destination, destination_airport, destination_airport_code, estimated_departure, age_type, base_price):
        '''Class Constructor method'''
        self.holder_name = holder_name
        self.airline = airline
        self.flight_code = flight_code
        self.destination = destination
        self.destination_airport = destination_airport
        self.destination_airport_code = destination_airport_code
        self.estimated_departure = estimated_departure
        self.age_type = age_type

        # Calculate the price of the user's ticket from the base price
        self.price = self.calculate_price(base_price)

    def calculate_price(self, base_price):
        '''Calculate price on ticket from base price for flight, as well as other factors'''

        # Start by setting the price as the base price for the flight
        price = int(base_price)
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
        '''Class Constructor method'''
        self.name = name
        self.email = email
        self.tickets = []           # List to store user's ticket

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
            output_str += "---------------------------------------------------------------------------------------------------------------------------------------------\n"

            # Create column headings
            output_str += "#  | Name                      | Airline            | Code  | Destination                            | Type   | Date/Time           | Price \n"
            output_str += "---|---------------------------|--------------------|-------|----------------------------------------|--------|---------------------|--------\n"
            
            for user_ticket in self.tickets:
                # Add each ticket in the user's order to the string
                output_str += (f"{self.tickets.index(user_ticket) + 1: <2} | {user_ticket.holder_name: <25} | {user_ticket.airline: <18} | {user_ticket.flight_code: <5} | {user_ticket.destination_airport: <38} | {str(user_ticket.age_type): <6} | {str(user_ticket.estimated_departure): <19} | ${user_ticket.price:.2f}\n")

            # Add an endline to the sring
            output_str += "---------------------------------------------------------------------------------------------------------------------------------------------\n"

            # Display the total price of the user's order
            output_str += f"Total: ${self.calculate_total_price():.2f}"

            return output_str

# Setup main window
root = Tk()
root.title("Flight Booking App")
root.geometry("700x400")

def create_ticket(flight_code, age, holder_name):
    '''Validate information entered by user and instantiate a ticket object'''
    
    # Used when checking that user has entered the code for a flight that exists
    flight_exists = False

    # Check the flight code entered by the user with the flight code of each
    # available flight. This is to make sure that the flight code entered by
    # the user corresponds to an actual flight that exists.
    for flight in flights:
        if flight.flight_code == flight_code:
            flight_exists = True
            chosen_flight = flight      # Store the flight chosen by the user in a new variable (chosen_flight)

    # If the user did not enter a valid flight code, tell them this, and return None so that
    # the function will stop executing.
    if flight_exists == False:
        messagebox.showinfo("Error", "Please enter a flight code that exists")
        return None

    # Convert the age entered by the user from the Entrybox to an integer value.
    # This must be done or else the program will not be able to work with the age
    # variable.
    age = int(age)
    age_type = StringVar()      # Used to store the age type of the ticket holder (e.g. Child, Adult, Senior)

    # Validate the user's input and/or determine the age type of the ticket holder.
    # Set the value of age_type accordingly.
    if age < 0:     # Start by checking that the user did not enter a negative number (Accept 0 as an age because a baby who is just born technically has an age equivalent of 0 years old.)
        # If the user entered a negative age, display a message and return None to exit the function.
        messagebox.showinfo("Error", "An age cannot be a negative number, please enter a real age.")    
        return None
    elif age <= MAX_CHILD_AGE:
        # If the age entered is not less than 0, we already know that it must be greater than or equal to zero,
        # so we just need to check that it is less than or equal to MAX_CHILD_AGE. That is, we do not need to
        # do: 
        # elif user_age >= 0 and user_age <= MAX_CHILD_AGE
        # Instead, for more succint code, we just need to test on the upper limit that user_age <= MAX_CHILD_AGE.
        age_type = "Child"
    elif age <= MAX_ADULT_AGE:
        age_type = "Adult"
    elif age <= MAX_SENIOR_AGE:
        age_type = "Senior"
    else:
        # If the user enters an age which is greater than the maximum senior age (i.e. an age that is 
        # unrealistically high), tell them to enter a real age and return None to exit the function.
        messagebox.showinfo("Error", "Please enter a real age.")
        return None

    # If the user did not enter a name, display a message and 
    # return None to exit the function
    if len(holder_name) == 0:
        messagebox.showinfo("Error", "Please enter a name.")
        return None

    # Iterate through each character in the user's name and check that it is either a character in the
    # alphabet, or it is one of the special characters that are allowed in a user's name.
    for character in holder_name:
        if character.isalpha() or character in ACCEPTED_SPECIAL_CHARACTERS:
            continue        # Character is valid, so continue to the next iteration of the loop to check the next character.
        else:
            # User's name contains an invalid character, so display a message and return None to exit the function.
            messagebox.showinfo("Error", "Your name contains non-alphabetic characters that are not accepted. Please enter a valid name.")
            return None

    # If the program reaches this point, it means that the details provided by the user have passed validation and so are correct.
    # Thus, instantiate a Ticket object with the relevant information and add it to the user's tickets.
    ticket = Ticket(holder_name, chosen_flight.airline, chosen_flight.flight_code, chosen_flight.destination, chosen_flight.destination_airport, chosen_flight.destination_airport_code, chosen_flight.estimated_departure, age_type, chosen_flight.base_price)
    user.add_ticket(ticket)

    # Check if the user's ticket qualified for a discount because of the ticket holder age.
    # If so, display a message to tell the user this, and then display another message as confirmation
    # for their ticket. Even if the user does not qualify for a discount based on their age,
    # still display a confirmation message for their ticket.
    if age_type == "Child":
        messagebox.showinfo("Discount information", f"This ticket qualifies for a Child's discount of {(1 - CHILD_TICKET_PRICE) * 100}%, bringing the price down to {ticket.price}.")
        messagebox.showinfo("Confirmation", f"Child's Ticket added to order.")
    elif age_type == "Senior":
        messagebox.showinfo("Discount information", f"This ticket qualifies for a Senior's discount of {(1 - SENIOR_TICKET_PRICE) * 100}%, bringing the price down to {ticket.price}.")
        messagebox.showinfo("Confirmation", f"Senior's Ticket added to order.")
    else:
        messagebox.showinfo("Confirmation", "Adult's Ticket added to order")

    # After having created a ticket, the user should return back to the main menu.
    # Thus, remove the booking flight frame with .destroy() and call the main_screen() function.
    book_flight_frame.destroy()
    main_screen()

def book_flight_screen():
    '''Screen for the user to book flights'''
    global book_flight_frame

    # Remove the main menu frame as the user is now on the book flights frame.
    main_frame.destroy()
    # Create the booking flights frame and use .pack() so that it is on the window
    # and takes up the entire window.
    book_flight_frame = Frame(root)
    book_flight_frame.pack(side = "top", fill = "both", expand = True)

    # Create the columns and rows as required for everything. Doing this manually means that I can
    # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
    # fix the uniformity problem that arises with the grid method.
    book_flight_frame.columnconfigure((0, 2), weight = 2, uniform = 'a')
    book_flight_frame.columnconfigure(1, weight = 7, uniform = 'a')
    book_flight_frame.rowconfigure(0, weight = 2, uniform = 'a')
    book_flight_frame.rowconfigure(1, weight = 10, uniform = 'a')
    book_flight_frame.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

    # Columns for table of flights
    column = ("Airline", "Code", "Destination", "Date/Time", "Price")

    # Create a Treeview widget for the table
    tree = ttk.Treeview(book_flight_frame, columns = column, show = "headings")

    # Enter the headings for each column in the table
    tree.heading('Airline', text='Airline')
    tree.heading('Code', text='Code')
    tree.heading('Destination', text='Destination')
    tree.heading('Date/Time', text='Date/Time')
    tree.heading('Price', text='Price')

    # List to store each flight/row of the table in (in tuple format)
    data = []

    # Iterate through each flight in the list of all flights and add a tuple for each
    # flight to the data list.
    for i in range(len(ALL_FLIGHTS)):
        data.append((f"{ALL_FLIGHTS[i][FLIGHT_AIRLINE]}", f"{ALL_FLIGHTS[i][FLIGHT_CODE]}", f"{ALL_FLIGHTS[i][FLIGHT_DEST]}", f"{ALL_FLIGHTS[i][FLIGHT_DEPT]}", f"${ALL_FLIGHTS[i][FLIGHT_BASE_PRICE]:.2f}"))

    # Insert each flight onto the tree
    for d in data:
        tree.insert('', END, values = d)

    # Use the grid method to put the tree table onto the window
    tree.grid(row=1, column=0, columnspan = 3, sticky='news')

    # Add a scrollbar to the table of flights
    scrollbar = ttk.Scrollbar(book_flight_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=3, sticky='nws')

    # Below are the labels for all of the text on this frame, as well as the entry boxes for user input.
    flight_text_lbl = Label(book_flight_frame, text = "Flight Code:", font = ("Arial", 10))
    flight_text_lbl.grid(row = 2, column = 1, sticky = "W")

    flight_text_entry = Entry(book_flight_frame)
    flight_text_entry.grid(row = 2, column = 1)

    age_text_lbl = Label(book_flight_frame, text = "Age:", font = ("Arial", 10))
    age_text_lbl.grid(row = 3, column = 1, sticky = "W")

    age_text_entry = Entry(book_flight_frame)
    age_text_entry.grid(row = 3, column = 1)
    
    name_text_lbl = Label(book_flight_frame, text = "Ticket holder Name:", font = ("Arial", 10))
    name_text_lbl.grid(row = 4, column = 1, sticky = "W")

    name_text_entry = Entry(book_flight_frame)
    name_text_entry.grid(row = 4, column = 1)

    # Button for when the user is finished entering information into the entry boxes.
    # Note that I had to use lambda in order for the command part of the button
    # to work with passing in inputs to the create_ticket() function.
    continue_btn = Button(book_flight_frame, text = "Continue", command = lambda:create_ticket(flight_text_entry.get(), age_text_entry.get(), name_text_entry.get()))
    continue_btn.grid(row = 5, column = 1)

def display_tickets_screen():
    '''Screen to display the user's tickets'''
    global display_tickets_frame

    # Remove the main frame for the frame to display tickets
    main_frame.destroy()

    # Create the ticket display frame and use .pack() so that it is on the window
    # and takes up the entire window.
    display_tickets_frame = Frame(root)
    display_tickets_frame.pack(side = "top", fill = "both", expand = True)

    # Configure the rows and columns for widgets on this frame. Doing this manually means that I can
    # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
    # fix the uniformity problem that arises with the grid method.
    display_tickets_frame.columnconfigure((0, 2), weight = 2, uniform = 'a')
    display_tickets_frame.columnconfigure(1, weight = 7, uniform = 'a')
    display_tickets_frame.rowconfigure(0, weight = 2, uniform = 'a')
    display_tickets_frame.rowconfigure(1, weight = 10, uniform = 'a')
    display_tickets_frame.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

    def exit_screen():
        '''Allow the user to return back to the main menu'''
        display_tickets_frame.destroy()         # Remove the display_tickets_frame
        main_screen()                           # Go back to the main menu

    # Columns for table of tickets
    column = ("#", "Name", "Airline", "Code", "Destination", "Type", "Date/Time", "Price")

    # Create a Treeview widget for the table
    tree = ttk.Treeview(display_tickets_frame, columns = column, show = "headings")

    # Enter the headings for each column in the table
    tree.heading('#', text='#')
    tree.heading('Name', text='Name')
    tree.heading('Airline', text='Airline')
    tree.heading('Code', text='Code')
    tree.heading('Destination', text='Destination')
    tree.heading('Type', text='Type')
    tree.heading('Date/Time', text='Date/Time')
    tree.heading('Price', text='Price')

    # List to store each ticket/row of the table in (in tuple format)
    data = []

    # Iterate through each ticket of the user's tickets and add a tuple for each
    # ticket to the data list.
    for i in range(len(user.tickets)):
        data.append((f"{i + 1}", f"{user.tickets[i].holder_name}", f"{user.tickets[i].airline}", f"{user.tickets[i].flight_code}", f"{user.tickets[i].destination}", f"{user.tickets[i].age_type}", f"{user.tickets[i].estimated_departure}", f"${user.tickets[i].price:.2f}"))

    # Insert each ticket onto the tree
    for d in data:
        tree.insert('', END, values = d)

    # Use the grid method to put the tree table onto the window
    tree.grid(row=1, column=0, columnspan = 3, sticky='news')

    # Add a scrollbar to the table of tickets
    scrollbar = ttk.Scrollbar(display_tickets_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=3, sticky='nws')

    # Button for the user to go back to the main menu
    close_btn = Button(display_tickets_frame, text = "Close", command = exit_screen)
    close_btn.grid(row = 3, column = 1)

def remove_tickets_screen():
    '''Screen to allow the user to remove tickets from their order'''
    global remove_tickets_frame

    # If the user's order is empty, tell them this and return to the main menu
    # Note that this should be done before removing the main menu frame, so that the
    # user does not feel like anything has changed, apart from the messagebox appearing.
    if len(user.tickets) == 0:
        messagebox.showinfo("Error", "You currently have no tickets in your order so none can be removed.")
        return None

    main_frame.destroy()        # Remove the main frame so that the remove tickets frame can be placed. (See previous commment for which this is not done at the start)

    # Create frame for ticket removal screen
    remove_tickets_frame = Frame(root)
    remove_tickets_frame.pack(side = "top", fill = "both", expand = True)

    # Configure the rows and columns of the ticket removal screen. Doing this manually means that I can
    # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
    # fix the uniformity problem that arises with the grid method.
    remove_tickets_frame.columnconfigure((0, 2), weight = 2, uniform = 'a')
    remove_tickets_frame.columnconfigure(1, weight = 7, uniform = 'a')
    remove_tickets_frame.rowconfigure(0, weight = 2, uniform = 'a')
    remove_tickets_frame.rowconfigure(1, weight = 10, uniform = 'a')
    remove_tickets_frame.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

    def remove_users_ticket():
        '''Remove ticket from order'''

        # Get the user's input for the ticket they wish to remove from their order.
        ticket_number = int(remove_text_entry.get())
        
        # Check that the number entered by the user corresponds to an actual ticket from their order. If not,
        # tell them this and return None to exit the function (the remove_users_ticket() function).
        if ticket_number < 1 or ticket_number > len(user.tickets):
            messagebox.showinfo("Error", "Please enter a number which corresponds to a ticket in your order.")
            return None
        
        # Remove the ticket specified by the user.
        # Note that we must remove the (i - 1)th ticket, rather than the ith ticket, because
        # the first ticket on the Treeview table has a number of 1, whereas the first ticket
        # in the tickets list is 0.
        user.remove_ticket(i - 1)
        messagebox.showinfo("Ticket removed", "Ticket has been removed from your order.")       # Display confirmation to the user.

        # Return back to the main menu by removing the ticket removal frame and calling main_screen()
        remove_tickets_frame.destroy()
        main_screen()

    # Columns for table of tickets
    column = ("#", "Name", "Airline", "Code", "Destination", "Type", "Date/Time", "Price")

    # Create a Treeview widget for the table
    tree = ttk.Treeview(remove_tickets_frame, columns = column, show = "headings")

    # Enter the headings for each column in the table
    tree.heading('#', text='#')
    tree.heading('Name', text='Name')
    tree.heading('Airline', text='Airline')
    tree.heading('Code', text='Code')
    tree.heading('Destination', text='Destination')
    tree.heading('Type', text='Type')
    tree.heading('Date/Time', text='Date/Time')
    tree.heading('Price', text='Price')

    # List to store each ticket/row of the table in (in tuple format)
    data = []

    # Iterate through each ticket in the user's tickets and add a tuple for each
    # ticket to the data list.
    for i in range(len(user.tickets)):
        data.append((f"{i + 1}", f"{user.tickets[i].holder_name}", f"{user.tickets[i].airline}", f"{user.tickets[i].flight_code}", f"{user.tickets[i].destination}", f"{user.tickets[i].age_type}", f"{user.tickets[i].estimated_departure}", f"${user.tickets[i].price:.2f}"))

    # Insert each ticket onto the tree
    for d in data:
        tree.insert('', END, values = d)

    # Use the grid method to put the tree table onto the window
    tree.grid(row=1, column=0, columnspan = 3, sticky='news')

    # Add a scrollbar to the table of tickets
    scrollbar = ttk.Scrollbar(remove_tickets_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=3, sticky='nws')

    # Label to tell the user to remove their ticket.
    remove_text_lbl = Label(remove_tickets_frame, text = "Ticket number: ", font = ("Arial", 10))
    remove_text_lbl.grid(row = 3, column = 1, sticky = "W")

    # Entry box for user to enter the ticket number.
    remove_text_entry = Entry(remove_tickets_frame)
    remove_text_entry.grid(row = 3, column = 1)

    # Button for when user has entered their ticket number.
    remove_btn = Button(remove_tickets_frame, text = "Remove", command = remove_users_ticket)
    remove_btn.grid(row = 4, column = 1)

def farewell_user():
    '''Farewell the user and quit the program'''

    # Display a farewell message and quit the program with quit().
    messagebox.showinfo("Farewell", "Have a nice day!")
    quit()

def finish_order_screen():
    '''Screen for when the user is finished their order'''
    global finish_order_frame

    # If the user's order is empty, tell them this and return None to exit the function.
    if len(user.tickets) == 0:
        messagebox.showinfo("Error", "Your order is empty so you cannot finish it.")
        return None
    
    # Remove the main frame for the finish order frame.
    # This is done after check that the user's order is empty, so that the main frame is not
    # accidentally removed if the user is not able to go to the finish order screen.
    main_frame.destroy()

    # Create the finish order frame and put on the window such that it fills up the entire screen.
    finish_order_frame = Frame(root)
    finish_order_frame.pack(side = "top", fill = "both", expand = True)

    # Configure the rows and columns for widgets. Doing this manually means that I can
    # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
    # fix the uniformity problem that arises with the grid method.
    finish_order_frame.columnconfigure((0, 2), weight = 2, uniform = 'a')
    finish_order_frame.columnconfigure(1, weight = 7, uniform = 'a')
    finish_order_frame.rowconfigure(0, weight = 2, uniform = 'a')
    finish_order_frame.rowconfigure(1, weight = 10, uniform = 'a')
    finish_order_frame.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

    def continue_command():
        '''Respond to the user pressing the button'''

        # Ask the user whether they want to make another order from a message box.
        response = messagebox.askquestion("Confirmation", "Would you like to make another order?")
        if response == "yes":
            # If the user wants to make another order, remove the finish order frame and take them to the login screen
            # with login_screen().
            finish_order_frame.destroy()
            login_screen()
        else:
            # If the user does not want to make another order, farewell them.
            farewell_user()

    # Label to display the user's name and email
    user_info_text_lbl = Label(finish_order_frame, text = f"Summary of Tickets by: {user.name} ({user.email})")
    user_info_text_lbl.grid(row = 0, column = 1)

    # Columns for table of tickets
    column = ("#", "Name", "Airline", "Code", "Destination", "Type", "Date/Time", "Price")

    # Create a Treeview widget for the table
    tree = ttk.Treeview(finish_order_frame, columns = column, show = "headings")

    # Enter the headings for each column in the table
    tree.heading('#', text='#')
    tree.heading('Name', text='Name')
    tree.heading('Airline', text='Airline')
    tree.heading('Code', text='Code')
    tree.heading('Destination', text='Destination')
    tree.heading('Type', text='Type')
    tree.heading('Date/Time', text='Date/Time')
    tree.heading('Price', text='Price')

    # List to store each ticket/row of the table in (in tuple format)
    data = []

    # Iterate through each ticket in the user's order and add a tuple for each
    # ticket to the data list.
    for i in range(len(user.tickets)):
        data.append((f"{i + 1}", f"{user.tickets[i].holder_name}", f"{user.tickets[i].airline}", f"{user.tickets[i].flight_code}", f"{user.tickets[i].destination}", f"{user.tickets[i].age_type}", f"{user.tickets[i].estimated_departure}", f"${user.tickets[i].price:.2f}"))

    # Insert each ticket onto the tree
    for d in data:
        tree.insert('', END, values = d)

    # Use the grid method to put the tree table onto the window
    tree.grid(row=1, column=0, columnspan = 3, sticky='news')

    # Add a scrollbar to the table of tickets
    scrollbar = ttk.Scrollbar(finish_order_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=3, sticky='nws')

    # Label to display the total price of the user's order
    total_price_lbl = Label(finish_order_frame, text = f"Total Price: ${user.calculate_total_price()}")
    total_price_lbl.grid(row = 3, column = 0)

    # Button for when the user wants to move on, either to quit the program, or to make another order.
    continue_btn = Button(finish_order_frame, text = "Continue", command = continue_command)
    continue_btn.grid(row = 3, column = 1)

    # Write user's ticket information to an external file
    with open("orders.txt", "a") as file:
        file.write(f"\nName: {user.name}\n")
        file.write(f"Email: {user.email}\n")
        file.write(f"{user.display_tickets()}\n")

def cancel_order():
    '''Verify whether the user wants to cancel their order and quit and act accordingly'''

    # Message box to take the user's input
    response = messagebox.askquestion("Confirmation", "Are you sure you would like to cancel your order and quit the program?")
    if response == "yes":
        # If the user wants to quit, farewell them.
        farewell_user()
    else:
        # If the user does not want to quit, return None to exit the function (and go back to the main menu).
        return None

def main_screen():
    '''Screen for the main menu of the program'''
    global main_frame

    # Create the Main frame
    main_frame = Frame(root)
    main_frame.pack(side = "top", fill = "both", expand = True)

    # Configure the rows and columns to be used in this frame. Doing this manually means that I can
    # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
    # fix the uniformity problem that arises with the grid method.
    main_frame.columnconfigure((0, 2), weight = 2, uniform = 'a')
    main_frame.columnconfigure(1, weight = 3, uniform = 'a')
    main_frame.rowconfigure(0, weight = 2, uniform = 'a')
    main_frame.rowconfigure((1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')

    # Labels for the text on the screen
    header_text_lbl = Label(main_frame, text = "Flight Booking App", font = ("Arial", 20))
    header_text_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 3)

    subheader_text_lbl = Label(main_frame, text = "What would you like to do?", font = ("Arial", 12))
    subheader_text_lbl.grid(row = 1, column = 1, sticky = "NEWS")

    # Buttons for each option the user can choose from.
    book_flight_btn = Button(main_frame, text = "Book Flight", command = book_flight_screen)
    book_flight_btn.grid(row = 2, column = 1, sticky = "WE")

    show_tickets_btn = Button(main_frame, text = "Show Tickets", command = display_tickets_screen)
    show_tickets_btn.grid(row = 3, column = 1, sticky = "WE")
    
    remove_ticket_btn = Button(main_frame, text = "Remove ticket from Order", command = remove_tickets_screen)
    remove_ticket_btn.grid(row = 4, column = 1, sticky = "WE")
    
    finish_order_btn = Button(main_frame, text = "Finish Order", command = finish_order_screen)
    finish_order_btn.grid(row = 5, column = 1, sticky = "WE")
    
    cancel_order_btn = Button(main_frame, text = "Cancel Order", command = cancel_order)
    cancel_order_btn.grid(row = 6, column = 1, sticky = "WE")

def login_screen():
    '''Screen for the user login'''
    global login_frame

    # Create a login frame
    login_frame = Frame(root)
    login_frame.pack(side = "top", fill = "both", expand = True)

    # Configure the rows and columns to be used in this frame. Doing this manually means that I can
    # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
    # fix the uniformity problem that arises with the grid method.
    login_frame.columnconfigure((0, 2), weight = 2, uniform = 'a')
    login_frame.columnconfigure(1, weight = 3, uniform = 'a')
    login_frame.rowconfigure(0, weight = 2, uniform = 'a')
    login_frame.rowconfigure((1, 2, 3, 4, 5), weight = 1, uniform = 'a')

    def user_login():
        '''Manage the user login part of the program'''
        global user

        # Get the user's input from the entry boxes
        user_name = name_entry.get()
        user_email = email_entry.get()

        # Used to help validate user input
        user_entered_valid_email = False

        # Start by checking that the user entered a name. If not, display a message and return None
        # to exit the user_login() function (this will bring the user back to the login screen).
        if len(user_name) == 0:
            messagebox.showinfo("Error", "Please enter a name.")
            return None

        # Iterate through each character in the user's name and check that it is either a character in the
        # alphabet, or it is one of the special characters that are allowed in a user's name.
        for character in user_name:
            if character.isalpha() or character in ACCEPTED_SPECIAL_CHARACTERS:
                continue
            else:
                # If the user's name is not valid, tell them this and return None to exit the function (to bring them back to the login screen).
                messagebox.showinfo("Error", "Your name contains non-alphabetic characters that are not accepted. Please enter a valid name.")
                return None

        # Iterate through each character in user's email address to check that there exists an '@'
        # symbol. Given that alphanumeric characters such as numbers, symbols, etc, are allowed in an email
        # address, characters that are not allowed in a name, it becomes more difficult to validate user input
        # for email addresses. However, ALL email addresses must have an @ symbol, so an email address that
        # does not must be invalid.
        for character in user_email:
            if character == '@':
                user_entered_valid_email = True
                break

        # If the user entered an invalid email, tell them to enter a valid email address,
        # and return None to exit the function (bring them back to the login screen).
        if user_entered_valid_email == False:
            messagebox.showinfo("Error", "Please enter a valid email address.")
            return None

        # If the program reaches this point, the user's name and email are valid, since they have passed all validation.
        # Thus, the program can instantiate the User object and continue to the main part of the program.
        user = User(user_name, user_email)

        # Destroy the login frame and go to the main frame.
        login_frame.destroy()
        main_screen()

    # Main header text
    header_lbl = Label(login_frame, text = "Welcome to the Flight Booking App!", font = ("Arial", 20))
    header_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 3)

    # Label and entry box for user's name
    name_lbl = Label(login_frame, text = "Please enter your name", font = ("Arial", 12))
    name_lbl.grid(row = 1, column = 1, sticky = "WENS")

    name_entry = Entry(login_frame)
    name_entry.grid(row = 2, column = 1, sticky = "WE")

    # Label and entry box for user's email
    email_lbl = Label(login_frame, text = "Please enter your email", font = ("Arial", 12))
    email_lbl.grid(row = 3, column = 1, sticky = "WENS")

    email_entry = Entry(login_frame)
    email_entry.grid(row = 4, column = 1, sticky = "WE")

    # Button for when user has finished entering information
    login_btn = Button(login_frame, text = "Continue", font = ("Arial", 9), command = user_login)
    login_btn.grid(row = 5, column = 1)

# List to store each flight as an object
flights = []

# For each flight, instantiate a Flight object for it and add it to the flights list
for flight in ALL_FLIGHTS:
    f = Flight(flight[FLIGHT_AIRLINE], flight[FLIGHT_CODE], flight[FLIGHT_DEST], flight[FLIGHT_DEST_AIRPORT], flight[FLIGHT_DEST_AIRPORT_CODE], flight[FLIGHT_DEPT], flight[FLIGHT_BASE_PRICE])

    flights.append(f)

# Display the login screen
login_screen()

# Where GUI is ended
root.mainloop()