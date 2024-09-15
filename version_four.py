# Date: 15/09/2024
# Author: Joshua Hutchings
# Version: 4
# Purpose: Create a program that allows the user to book a plane flight

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Image: https://www.flickr.com/photos/umedhairesha/6756372125
from PIL import Image, ImageTk
from datetime import datetime

import csv
import json

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

# Main background colour for each screen, used in most elements so that they have the same background
# colour as the screen that they are on.
MAIN_BG_COLOUR = "#DAE8FC"

# Class to store all of the information about each ticket, as well as calculate the price, etc.
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

# Class to store all the information about a user, as well as manage their tickets, calculate the total price, etc.
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

# Class to manage the program and the GUI, such as the different screens, etc.
class App(Tk):
    # Class constant variables used to refer to each screen/frame in the program
    LOGIN_SCREEN = 0
    ACCOUNT_LOGIN_SCREEN = 1
    ACCOUNT_CREATION_SCREEN = 2
    MAIN_MENU_SCREEN = 3
    BOOK_FLIGHTS_SCREEN = 4
    VIEW_TICKETS_SCREEN = 5
    REMOVE_TICKETS_SCREEN = 6
    FINISH_ORDER_SCREEN = 7

    # Stores the User object when instantiated. This is so that
    # it does not need to be made a global variable, but can
    # still be accessed by everything that requires it.
    user = None

    # Stores all of the flights available for the user to book
    ALL_FLIGHTS = []

    def __init__(self):
        '''Class constructor method'''
        super().__init__()              # This is needed to properly initialise the Tk class properly
        self.title("Flight Booking App")
        self.geometry("700x400")
        self.resizable(False, False)
        self.current_frame = None       # Initially, there is no frame, so hence initialise this to None
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        # Gets the flights from the csv file and saves them to the ALL_FLIGHTS list
        self.ALL_FLIGHTS = self.get_flights()

        # Show the login screen frame since this will be what the user
        # should go on once they first start the program.
        self.show_frame(self.LOGIN_SCREEN)

    def show_frame(self, frame_index):
        '''Switch to the specified frame'''

        # Check which frame index has been passed to the function,
        # to determine which screen the program is trying to go to.
        # Depending on which screen it is, either destroy the current
        # frame and then change current_frame to match the new screen, 
        # or first check that the program is able to go to the desired
        # screen.

        # Check that the current frame is defined before trying to destroy
        # # it (to avoid any unexpected crashes).
        if frame_index == App.LOGIN_SCREEN:
            if self.current_frame:
                self.current_frame.destroy()
            self.current_frame = LoginScreen(self)

        elif frame_index == App.ACCOUNT_LOGIN_SCREEN:
            if self.current_frame:
                self.current_frame.destroy()
            self.current_frame = AccountLoginScreen(self)

        elif frame_index == App.ACCOUNT_CREATION_SCREEN:
            if self.current_frame:
                self.current_frame.destroy()
            self.current_frame = AccountCreationScreen(self)

        elif frame_index == App.MAIN_MENU_SCREEN:
            if self.current_frame:
                self.current_frame.destroy()
            self.current_frame = MainMenuScreen(self)

        elif frame_index == App.BOOK_FLIGHTS_SCREEN:
            if self.current_frame:
                self.current_frame.destroy()
            self.current_frame = BookFlightsScreen(self)

        elif frame_index == App.VIEW_TICKETS_SCREEN:
            if self.current_frame:
                self.current_frame.destroy()
            self.current_frame = ViewTicketsScreen(self)

        elif frame_index == App.REMOVE_TICKETS_SCREEN:
            # If the user's order is empty, tell them this and do not go to the Remove tickets screen.
            if len(app.user.tickets) == 0:
                messagebox.showinfo("Error", "Your order is empty so you have no tickets to remove.")
                return None                 # Return None so as to exit the method.
            if self.current_frame:
                self.current_frame.destroy()
            self.current_frame = RemoveTicketsScreen(self)

        elif frame_index == App.FINISH_ORDER_SCREEN:
            # Start by checking if the user's order is empty, and if so, display a message
            # and do not take them to the Finish order screen.
            if len(app.user.tickets) == 0:
                messagebox.showinfo("Error", "Your order is empty so you cannot finish it.")
                return None         # Return None so that the function stops executing, and does not try to
            else:                   # put the same frame on the screen again (last line of function)
                if self.current_frame:
                    self.current_frame.destroy()
                self.current_frame = FinishOrderScreen(self)

        # Use the .grid() method to put the new frame on the screen where it is fullscreen/takes up the full window.
        self.current_frame.grid(row = 0, column = 0, sticky = "NEWS")

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

    def get_flights(self):
        '''Gets the flights from the csv file'''

        # Stores a list of all flights the user can choose from
        all_flights = []

        # Opens the csv file storing the flights and loads them into the ALL_FLIGHTS list.
        with open('flights.csv', mode = 'r') as file:
            csvFile = csv.reader(file)

            # Used to check if the line being iterated through is not the first line of the csv file.
            # This is because, the first line contains the column headings, which are unnecessary to be
            # stored in the all_flights list.
            first_line = True

            # Iterate through each line of the file
            for lines in csvFile:
                # Check that the line being iterated through is not the first line, and if it is,
                # skip it.
                if first_line:
                    first_line = False
                    continue
                
                # Convert the departure date/time into a datetime object.
                # Credit: https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
                date_string = lines[-2]
                date_time_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
                lines[-2] = date_time_obj

                # Convert the base price from a string to a float.
                lines[-1] = float(lines[-1])

                # Add the current line/flight to the all_flights list.
                all_flights.append(lines)

        # Return the list of the flights
        return all_flights

class LoginScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Set the background colour
        self.configure(background = MAIN_BG_COLOUR)

        # Configure the rows and columns to be used in this frame.
        self.columnconfigure((0, 2), weight=2, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure(0, weight=5, uniform='a')
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='a')

        main_image = ImageTk.PhotoImage(Image.open("menu_image.jpg"))
        main_image_label = Label(self, bg="#ffffff", image=main_image)
        main_image_label.image = main_image
        main_image_label.grid(row = 0, column = 1)

        # Main header text
        header_lbl = Label(self, text="Welcome to the Flight Booking App!", font=("Arial", 20, "bold"), background = MAIN_BG_COLOUR)
        header_lbl.grid(row=1, column=0, sticky="NEWS", columnspan=3)

        subtext_lbl = Label(self, text="What would you like to do?", font=("Arial", 13, "bold"), background = MAIN_BG_COLOUR)
        subtext_lbl.grid(row=2, column=1, sticky="WE")

        login_screen_btn = Button(self, text="Login", font = ("bold"), command = lambda: app.show_frame(App.ACCOUNT_LOGIN_SCREEN))
        login_screen_btn.grid(row=4, column=0)

        create_account_btn = Button(self, text="Create Account", command = lambda: app.show_frame(App.ACCOUNT_CREATION_SCREEN))
        create_account_btn.grid(row=4, column=1)

        bottom_label = Label(self)
        bottom_label.grid(row = 6, column = 0, columnspan = 3, sticky = "NEWS")

class AccountLoginScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Load the json accounts file
        with open("accounts.json", "r") as f:
            self.accounts = json.load(f)

        # Configure the rows and columns to be used in this frame.
        self.columnconfigure((0, 2), weight=2, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure((1, 2, 3, 4, 5), weight=1, uniform='a')

        # Main header text
        header_lbl = Label(self, text="Welcome to the Flight Booking App!", font=("Arial", 20))
        header_lbl.grid(row=0, column=0, sticky="NEWS", columnspan=3)

        # Label and entry box for user's email address
        email_lbl = Label(self, text="Please enter your email", font=("Arial", 12))
        email_lbl.grid(row=1, column=1, sticky="WENS")

        self.email_entry = Entry(self)
        self.email_entry.grid(row=2, column=1, sticky="WE")

        # Label and entry box for user's password
        password_lbl = Label(self, text="Please enter your password", font=("Arial", 12))
        password_lbl.grid(row=3, column=1, sticky="WENS")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=4, column=1, sticky="WE")

        # Button for when the user has finished entering information
        login_btn = Button(self, text="Continue", font=("Arial", 9), command=self.user_login)
        login_btn.grid(row=5, column=1)

    def user_login(self):
        '''Manage the user login part of the program'''
        user_email = self.email_entry.get()
        user_password = self.password_entry.get()

        # Start by checking that the user entered an email and password. If not, display a message and return None
        # to exit the user_login() method (this will bring the user back to the login screen).
        if len(user_email) == 0 or len(user_password) == 0:
            messagebox.showinfo("Error", "Please enter your email and/or password.")
            return None

        # Check that the user entered the email address for an account that exists.
        # This variable will become True if an account is found with the same email
        # address that the user entered.
        account_exists = False

        # Stores the user's account if it is found.
        user_account = None

        # Iterate through each account and see if it has an email address which matches
        # what the user typed in.
        for account in self.accounts["accounts"]:
            if account["email"] == user_email:
                user_account = account
                account_exists = True
                break

        # Tell the user that there are no accounts that could be found with their email,
        # and return None to exit the user_login() method.
        if not account_exists:
            messagebox.showinfo("Account not found", "No accounts were found with your email. Please ensure you have entered the correct email.")
            return None

        # Check that the user's password is correct.
        # If not, display a message and return None to exit the user_login() method.
        if user_account["password"] != user_password:
            messagebox.showinfo("Incorrect Password", "The password you have entered is incorrect.")
            return None
        else:
            # Welcome the user (their password is correct).
            messagebox.showinfo("Welcome", f"Welcome {user_account['name']}!")

        # Instantiate the User object and continue to the main part of the program.
        app.user = User(user_account["name"], user_account["email"])
        app.show_frame(App.MAIN_MENU_SCREEN)

class AccountCreationScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the rows and columns to be used in this frame.
        self.columnconfigure((0, 2), weight=2, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure((0, 1), weight=2, uniform='a')
        self.rowconfigure((2, 3, 4, 5, 6, 7, 8), weight=1, uniform='a')

        # Main header text
        header_lbl = Label(self, text="Welcome to the Flight Booking App!", font=("Arial", 20))
        header_lbl.grid(row=0, column=0, sticky="NEWS", columnspan=3)

        sub_header_lbl = Label(self, text = "Please enter the following information", font = ("Arial", 12))
        sub_header_lbl.grid(row = 1, column = 1, sticky = "EW")

        # Label and entry box for user's name
        name_lbl = Label(self, text = "Name", font = ("Arial", 10))
        name_lbl.grid(row = 2, column = 1, sticky = "NEWS")

        self.name_entry = Entry(self)
        self.name_entry.grid(row = 3, column = 1, sticky = "WE")
        
        # Label and entry box for user's email
        email_lbl = Label(self, text = "Email", font = ("Arial", 10))
        email_lbl.grid(row = 4, column = 1, sticky = "NEWS")

        self.email_entry = Entry(self)
        self.email_entry.grid(row = 5, column = 1, sticky = "WE")
        
        # Label and entry box for user's password
        password_lbl = Label(self, text = "Password", font = ("Arial", 10))
        password_lbl.grid(row = 6, column = 1, sticky = "NEWS")

        self.password_entry = Entry(self)
        self.password_entry.grid(row = 7, column = 1, sticky = "WE")

        # Button to create account when user has finished entering information
        create_account_btn = Button(self, text = "Create Account", font = ("Arial", 9), command = self.user_create_account)
        create_account_btn.grid(row = 8, column = 1)

    def user_create_account(self):
        '''Manage the account creation part of the program'''

        user_name = self.name_entry.get()
        user_email = self.email_entry.get()
        user_password = self.password_entry.get()

        if len(user_name) == 0 or len(user_email) == 0 or len(user_password) == 0:
            messagebox.showinfo("Incomplete section(s)", "Please complete the form by filling in each section.")
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
        
        # Used to help validate user input
        user_entered_valid_email = False

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
            messagebox.showinfo("Error", "Your email does not have an '@' symbol. Please enter a valid email address.")
            return None

        # Now check that the user has a full stop in their email address.
        # Repeat the same process as before of iterating through each character in their
        # email address, though this time check for any full stop characters.
        user_entered_valid_email = False
        for character in user_email:
            if character == '.':
                user_entered_valid_email = True
                break

        # If the user does not have any full stops in their email address, tell them to
        # enter a valid email and exit the function to bring them back to the login screen.
        if user_entered_valid_email == False:
            messagebox.showinfo("Error", "Your email does not have any full stops. Please enter a valid email address.")
            return None
        
        self.write_user_to_file(user_name, user_email, user_password)
        # Instantiate the User object and continue to the main part of the program.
        app.user = User(user_name, user_email)
        app.show_frame(App.MAIN_MENU_SCREEN)

    def write_user_to_file(self, user_name, user_email, user_password):
        '''Write the user's account information to a file'''

        # Open the accounts file to update it.
        with open("accounts.json") as f:
            data = json.load(f)

        # Add the account information to the data dictionary.
        data["accounts"].append({"name": user_name, "email": user_email, "password": user_password})

        # Write the updated info to the file.
        with open("accounts.json", "w") as f:
            json.dump(data, f, indent = 4)

        # Tell the user that their account has been created.
        messagebox.showinfo("Confirmation", f"Account created successfully, Welcome {user_name}!")

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

class BookFlightsScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the columns and rows as required for everything. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 10, uniform = 'a')
        self.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

        # Back button for the user to return to the main menu
        back_btn = Button(self, text = "Back", command = lambda: app.show_frame(App.MAIN_MENU_SCREEN))
        back_btn.grid(row = 0, column = 0)

        # Columns for table of flights
        column = ("Airline", "Code", "Destination", "Date/Time", "Price")

        # Create a Treeview widget for the table
        tree = ttk.Treeview(self, columns = column, show = "headings")

        tree.column("Airline", minwidth = 110, width = 120, anchor='center')
        tree.column("Code", minwidth = 50, width = 65, anchor='center')
        tree.column("Destination", minwidth = 175, width = 230, anchor='center')
        tree.column("Date/Time", minwidth = 125, width = 160, anchor='center')
        tree.column("Price", minwidth = 60, width = 100, anchor='center')

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
        for i in range(len(app.ALL_FLIGHTS)):
            data.append((f"{app.ALL_FLIGHTS[i][FLIGHT_AIRLINE]}", f"{app.ALL_FLIGHTS[i][FLIGHT_CODE]}", f"{app.ALL_FLIGHTS[i][FLIGHT_DEST]}", f"{app.ALL_FLIGHTS[i][FLIGHT_DEPT]}", f"${app.ALL_FLIGHTS[i][FLIGHT_BASE_PRICE]:.2f}"))

        # Insert each flight onto the tree
        for d in data:
            tree.insert('', END, values = d)

        # Use the grid method to put the tree table onto the window
        tree.grid(row=1, column=0, columnspan = 3, sticky='news')

        # Add a scrollbar to the table of flights
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky='nws')

        # Used to determine when the user has selected a flight, and which flight it is.
        self.selected_flight_code = None

        def on_row_select(event):
            # Get the selected item
            selected_item = tree.selection()[0]
            values = tree.item(selected_item, "values")
            self.selected_flight_code = str(values[1])

        # Bind the TreeView selection event
        tree.bind("<<TreeviewSelect>>", on_row_select)

        # Below are the labels for all of the text on this frame, as well as the entry boxes for user input.
        flight_text_lbl = Label(self, text = "Click the flight to select it", font = ("Arial", 10))
        flight_text_lbl.grid(row = 2, column = 1, sticky = "W")

        age_text_lbl = Label(self, text = "Age:", font = ("Arial", 10))
        age_text_lbl.grid(row = 3, column = 1, sticky = "W")

        age_text_entry = Entry(self)
        age_text_entry.grid(row = 3, column = 1)

        name_text_lbl = Label(self, text = "Ticket holder Name:", font = ("Arial", 10))
        name_text_lbl.grid(row = 4, column = 1, sticky = "W")

        name_text_entry = Entry(self)
        name_text_entry.grid(row = 4, column = 1)
        
        # Button for when the user is finished entering information into the entry boxes.
        # Note that I had to use lambda in order for the command part of the button
        # to work with passing in inputs to the create_ticket() function.
        continue_btn = Button(self, text = "Continue", command = lambda: self.create_ticket(self.selected_flight_code, age_text_entry.get(), name_text_entry.get()))
        continue_btn.grid(row = 5, column = 1)

    def create_ticket(self, flight_code, age, holder_name):
        '''Validate information entered by user and instantiate a ticket object'''

        # If the user did not select a flight, tell them this, and return None so that
        # the function will stop executing.
        if flight_code == None:
            messagebox.showinfo("Error", "Please select a flight.")
            return None
        
        for flight in app.ALL_FLIGHTS:
                   if flight[FLIGHT_CODE] == flight_code:
                       chosen_flight = flight      # Store the flight chosen by the user in a new variable (chosen_flight)

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
        ticket = Ticket(holder_name, chosen_flight[FLIGHT_AIRLINE], chosen_flight[FLIGHT_CODE], chosen_flight[FLIGHT_DEST], chosen_flight[FLIGHT_DEST_AIRPORT], chosen_flight[FLIGHT_DEST_AIRPORT_CODE], chosen_flight[FLIGHT_DEPT], age_type, chosen_flight[FLIGHT_BASE_PRICE])
        app.user.add_ticket(ticket)

        # Check if the user's ticket qualified for a discount because of the ticket holder age.
        # If so, display a message to tell the user this, and then display another message as confirmation
        # for their ticket. Even if the user does not qualify for a discount based on their age,
        # still display a confirmation message for their ticket.
        if age_type == "Child":
            messagebox.showinfo("Discount information", f"This ticket qualifies for a Child's discount of {(1 - CHILD_TICKET_PRICE) * 100}%, bringing the price down to ${ticket.price:.2f}.")
            messagebox.showinfo("Confirmation", f"Child's Ticket added to order.")
        elif age_type == "Senior":
            messagebox.showinfo("Discount information", f"This ticket qualifies for a Senior's discount of {(1 - SENIOR_TICKET_PRICE) * 100}%, bringing the price down to ${ticket.price:.2f}.")
            messagebox.showinfo("Confirmation", f"Senior's Ticket added to order.")
        else:
            messagebox.showinfo("Confirmation", "Adult's Ticket added to order")

        BookFlightsScreen.grid_remove(self)
        # After having created a ticket, the user should return back to the main menu.
        # Thus, remove the booking flight frame with .destroy() and call the main_screen() function.
        app.show_frame(App.MAIN_MENU_SCREEN)

class ViewTicketsScreen(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Configure the rows and columns for widgets on this frame. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 10, uniform = 'a')
        self.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

        '''Create the widgets for this windows'''
        # Columns for table of tickets
        column = ("Name", "Airline", "Code", "Destination", "Type", "Date/Time", "Price")

        # Create a Treeview widget for the table
        tree = ttk.Treeview(self, columns = column, show = "headings")

        tree.column("Name", minwidth = 80, width = 90, anchor = 'center')
        tree.column("Airline", minwidth = 110, width = 120, anchor='center')
        tree.column("Code", minwidth = 50, width = 50, anchor='center')
        tree.column("Destination", minwidth = 175, width = 185, anchor='center')
        tree.column("Type", minwidth = 50, width = 50, anchor='center')
        tree.column("Date/Time", minwidth = 125, width = 125, anchor='center')
        tree.column("Price", minwidth = 60, width = 60, anchor='center')

        # Enter the headings for each column in the table
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
        for i in range(len(self.master.user.tickets)):
            data.append((f"{self.master.user.tickets[i].holder_name}", f"{self.master.user.tickets[i].airline}", f"{self.master.user.tickets[i].flight_code}", f"{self.master.user.tickets[i].destination}", f"{self.master.user.tickets[i].age_type}", f"{self.master.user.tickets[i].estimated_departure}", f"${self.master.user.tickets[i].price:.2f}"))

        # Insert each ticket onto the tree
        for d in data:
            tree.insert('', END, values = d)

        # Use the grid method to put the tree table onto the window
        tree.grid(row=1, column=0, columnspan = 3, sticky='news')

        # Add a scrollbar to the table of tickets
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky='nws')

        # Button for the user to go back to the main menu
        close_btn = Button(self, text = "Close", command = self.exit_screen)
        close_btn.grid(row = 3, column = 1)

    def exit_screen(self):
        '''Allow the user to return back to the main menu'''
        
        app.show_frame(App.MAIN_MENU_SCREEN)

class RemoveTicketsScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the rows and columns of the ticket removal screen. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 10, uniform = 'a')
        self.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

        # Back button for the user to return to the main menu
        back_btn = Button(self, text = "Back", command = lambda: app.show_frame(App.MAIN_MENU_SCREEN))
        back_btn.grid(row = 0, column = 0)

        # Columns for table of tickets
        column = ("Name", "Airline", "Code", "Destination", "Type", "Date/Time", "Price")

        # Enter the headings for each column in the table
        tree = ttk.Treeview(self, columns = column, show = "headings")
        
        tree.column("Name", minwidth = 80, width = 90, anchor = 'center')
        tree.column("Airline", minwidth = 110, width = 120, anchor='center')
        tree.column("Code", minwidth = 50, width = 50, anchor='center')
        tree.column("Destination", minwidth = 175, width = 185, anchor='center')
        tree.column("Type", minwidth = 50, width = 50, anchor='center')
        tree.column("Date/Time", minwidth = 125, width = 125, anchor='center')
        tree.column("Price", minwidth = 60, width = 60, anchor='center')
        
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
        for i in range(len(app.user.tickets)):
            data.append((f"{app.user.tickets[i].holder_name}", f"{app.user.tickets[i].airline}", f"{app.user.tickets[i].flight_code}", f"{app.user.tickets[i].destination}", f"{app.user.tickets[i].age_type}", f"{app.user.tickets[i].estimated_departure}", f"${app.user.tickets[i].price:.2f}"))

        # Insert each ticket onto the tree
        for d in data:
            tree.insert('', END, values = d)

        # Use the grid method to put the tree table onto the window
        tree.grid(row=1, column=0, columnspan = 3, sticky='news')

        # Add a scrollbar to the table of tickets

        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky='nws')

        # Used to determine when the user has selected a flight, and which flight it is.
        self.selected_flight_code = None

        def on_row_select(event):
            # Get the selected item
            selected_item = tree.selection()[0]
            values = tree.index(selected_item)
            self.selected_flight_code = int(values)

        # Bind the TreeView selection event
        tree.bind("<<TreeviewSelect>>", on_row_select)

        # Label to tell the user to remove their ticket.
        remove_text_lbl = Label(self, text = "Select the ticket you wish to remove", font = ("Arial", 10))
        remove_text_lbl.grid(row = 3, column = 1, sticky = "W")

        # Button for when user has entered their ticket number.
        remove_btn = Button(self, text = "Remove", command = lambda: self.remove_users_ticket(self.selected_flight_code))
        remove_btn.grid(row = 4, column = 1)

    def remove_users_ticket(self, ticket_to_remove):
        '''Remove ticket from order'''
        
        # If the user did not select a flight, tell them this, and return None so that
        # the function will stop executing.
        if ticket_to_remove == None:
            messagebox.showinfo("Error", "Please select a flight.")
            return None
        
        #ticket_to_remove = ticket_to_remove.split(',')
    
        # Remove the ticket specified by the user.
        app.user.remove_ticket(ticket_to_remove)

        messagebox.showinfo("Ticket removed", "Ticket has been removed from your order.")       # Display confirmation to the user.
        app.show_frame(App.MAIN_MENU_SCREEN)

class FinishOrderScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the rows and columns for widgets. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 10, uniform = 'a')
        self.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

        # Label to display the user's name and email
        user_info_text_lbl = Label(self, text = f"Summary of Tickets by: {app.user.name} ({app.user.email})")
        user_info_text_lbl.grid(row = 0, column = 1)

        # Columns for table of tickets
        column = ("Name", "Airline", "Code", "Destination", "Type", "Date/Time", "Price")

        # Create a Treeview widget for the table
        tree = ttk.Treeview(self, columns = column, show = "headings")

        tree.column("Name", minwidth = 80, width = 90, anchor = 'center')
        tree.column("Airline", minwidth = 110, width = 120, anchor='center')
        tree.column("Code", minwidth = 50, width = 50, anchor='center')
        tree.column("Destination", minwidth = 175, width = 185, anchor='center')
        tree.column("Type", minwidth = 50, width = 50, anchor='center')
        tree.column("Date/Time", minwidth = 125, width = 125, anchor='center')
        tree.column("Price", minwidth = 60, width = 60, anchor='center')
        
        # Enter the headings for each column in the table
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
        for i in range(len(app.user.tickets)):
            data.append((f"{app.user.tickets[i].holder_name}", f"{app.user.tickets[i].airline}", f"{app.user.tickets[i].flight_code}", f"{app.user.tickets[i].destination}", f"{app.user.tickets[i].age_type}", f"{app.user.tickets[i].estimated_departure}", f"${app.user.tickets[i].price:.2f}"))

        # Insert each ticket onto the tree
        for d in data:
            tree.insert('', END, values = d)

        # Use the grid method to put the tree table onto the window
        tree.grid(row=1, column=0, columnspan = 3, sticky='news')

        # Add a scrollbar to the table of tickets
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky='nws')

        # Label to display the total price of the user's order
        total_price_lbl = Label(self, text = f"Total Price: ${app.user.calculate_total_price()}")
        total_price_lbl.grid(row = 3, column = 0)

        # Button for when the user wants to move on, either to quit the program, or to make another order.
        continue_btn = Button(self, text = "Continue", command = self.continue_command)
        continue_btn.grid(row = 3, column = 1)

        # Write user's ticket information to an external file
        with open("orders.txt", "a") as file:
            file.write(f"\nName: {app.user.name}\n")
            file.write(f"Email: {app.user.email}\n")
            file.write(f"{app.user.display_tickets()}\n")

    def continue_command(self):
        '''Respond to the user pressing the button'''

        # Ask the user whether they want to make another order from a message box.
        response = messagebox.askquestion("Confirmation", "Would you like to make another order?")
        if response == "yes":
            # If the user wants to make another order, remove the finish order frame and take them to the login screen
            # with login_screen().
            app.show_frame(App.LOGIN_SCREEN)
        else:
            # If the user does not want to make another order, farewell them.
            app.farewell_user()

# Setup main window
app = App()
app.mainloop()