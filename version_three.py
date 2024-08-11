# Date: 07/08/2024
# Author: Joshua Hutchings
# Version: 3
# Purpose: Create a program that allows the user to book a plane flight

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from datetime import datetime

# Constants to be used when accessing the data of flights, so as to improve code readability
FLIGHT_AIRLINE           = 0
FLIGHT_CODE              = 1
FLIGHT_DEST              = 2
FLIGHT_DEST_AIRPORT      = 3
FLIGHT_DEST_AIRPORT_CODE = 4
FLIGHT_DEPT              = 5
FLIGHT_BASE_PRICE        = 6

# Constants to be used when calculating the ticket prices for different age groups
CHILD_TICKET_PRICE = 0.75
ADULT_TICKET_PRICE = 1.00       # No discounts for Adults
SENIOR_TICKET_PRICE = 0.60

# Characters that are not in the alphabet, but that are allowed in a user's name
ACCEPTED_SPECIAL_CHARACTERS = ["-", ".", " ", "'"]

ALL_FLIGHTS = [
    ["Air New Zealand", "NZ101", "Wellington, New Zealand", "Wellington International Airport", "WLG", datetime(2024, 7, 10, 6, 30), 150.0],
    ["Qantas", "QF122", "Sydney, Australia", "Sydney Kingsford Smith Airport", "SYD", datetime(2024, 7, 10, 7, 45), 350.0],
    ["Jetstar", "JQ201", "Melbourne, Australia", "Melbourne Airport", "MEL", datetime(2024, 7, 10, 8, 15), 300.0],
]

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

class App(Tk):
    # Class constant variables used to refer to each screen/frame in the program
    # Each of these constants stores the index for a particular screen/frame
    # in a list of frames (see the init method)
    LOGIN_SCREEN = 0
    MAIN_MENU_SCREEN = 1
    BOOK_FLIGHTS_SCREEN = 2
    VIEW_TICKETS_SCREEN = 3
    REMOVE_TICKETS_SCREEN = 4
    FINISH_ORDER_SCREEN = 5

    def __init__(self):
        '''Class constructor method'''
        super().__init__()              # This is needed to properly initialise the Tk class properly
        self.title("Flight Booking App")
        self.geometry("700x400")
        self.frames = []
        self.current_frame = None       # Initially, there is no frame, so hence initialise this to None

        # Initialize all frames
        self.frames.append(LoginScreen(self))
        self.frames.append(MainMenuScreen(self))
        #self.frames.append(SettingsScreen(self))

        # Show the login screen frame since this will be what the user
        # should go on once they first start the program.
        self.show_frame(self.LOGIN_SCREEN)

    def show_frame(self, frame_index):
        '''Switch to the specified frame'''

        # Hide the frame of the current screen (though check that it actually
        # is defined first to avoid any unexpected crashes)
        if self.current_frame:
            self.current_frame.pack_forget()

        # Set the current frame to the frame which has been specified
        self.current_frame = self.frames[frame_index]
        # Use the .pack() method to put the new frame on the screen where it is fullscreen/takes up the full window.
        self.current_frame.pack(side="top", fill="both", expand=True)

    def quit_program(self):
        '''Verify whether the user wants to cancel their order and quit and act accordingly'''

        # Message box to take the user's input
        response = messagebox.askquestion("Confirmation", "Are you sure you would like to cancel your order and quit the program?")
        if response == "yes":
            # If the user wants to quit, farewell them.
            self.farewell_user()
        else:
            # If the user does not want to quit, return None to exit the function (and go back to the main menu).
            return None

    def farewell_user(self):
        '''Farewell the user and quit the program'''

        # Display a farewell message and quit the program with quit().
        messagebox.showinfo("Farewell", "Have a nice day!")
        quit()

class LoginScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the rows and columns to be used in this frame. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 3, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure((1, 2, 3, 4, 5), weight = 1, uniform = 'a')

        # Main header text
        header_lbl = Label(self, text = "Welcome to the Flight Booking App!", font = ("Arial", 20))
        header_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 3)

        # Label and entry box for user's name
        name_lbl = Label(self, text = "Please enter your name", font = ("Arial", 12))
        name_lbl.grid(row = 1, column = 1, sticky = "WENS")

        name_entry = Entry(self)
        name_entry.grid(row = 2, column = 1, sticky = "WE")

        # Label and entry box for user's email
        email_lbl = Label(self, text = "Please enter your email", font = ("Arial", 12))
        email_lbl.grid(row = 3, column = 1, sticky = "WENS")

        email_entry = Entry(self)
        email_entry.grid(row = 4, column = 1, sticky = "WE")

        # Button for when user has finished entering information
        login_btn = Button(self, text = "Continue", font = ("Arial", 9), command = lambda:self.user_login(name_entry.get(), email_entry.get()))
        login_btn.grid(row = 5, column = 1)

    def user_login(self, user_name, user_email):
        '''Manage the user login part of the program'''
        global user

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
        app.show_frame(App.MAIN_MENU_SCREEN)

class MainMenuScreen(Frame):
    def __init__(self, master):
        super().__init__(master)
        # Configure the rows and columns to be used in this frame. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 3, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')

        # Labels for the text on the screen
        header_text_lbl = Label(self, text = "Flight Booking App", font = ("Arial", 20))
        header_text_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 3)

        subheader_text_lbl = Label(self, text = "What would you like to do?", font = ("Arial", 12))
        subheader_text_lbl.grid(row = 1, column = 1, sticky = "NEWS")

        # Buttons for each option the user can choose from.
        book_flight_btn = Button(self, text = "Book Flight", command = lambda: app.show_frame(App.BOOK_FLIGHTS_SCREEN))
        book_flight_btn.grid(row = 2, column = 1, sticky = "WE")

        show_tickets_btn = Button(self, text = "Show Tickets", command = lambda: app.show_frame(App.VIEW_TICKETS_SCREEN))
        show_tickets_btn.grid(row = 3, column = 1, sticky = "WE")

        remove_ticket_btn = Button(self, text = "Remove ticket from Order", command = lambda: app.show_frame(App.REMOVE_TICKETS_SCREEN))
        remove_ticket_btn.grid(row = 4, column = 1, sticky = "WE")

        finish_order_btn = Button(self, text = "Finish Order", command = lambda: app.show_frame(App.FINISH_ORDER_SCREEN))
        finish_order_btn.grid(row = 5, column = 1, sticky = "WE")

        cancel_order_btn = Button(self, text = "Cancel Order", command = lambda: app.quit_program())
        cancel_order_btn.grid(row = 6, column = 1, sticky = "WE")


# Setup main window
app = App()
app.mainloop()