# Date: 20/09/2024
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

# The minimum length that a user's password can be. Used when the user creates their account to ensure
# that they choose a secure enough password.
MIN_PASSWORD_LENGTH = 8

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
    ACCOUNT_CREATION_SCREEN_TWO = 8
    BOOK_FLIGHTS_SCREEN_TWO = 9

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

        # Create a dictionary that stores the a reference to the class object for each screen.
        # This is used for switching between screens, as the number corresponding to a particular screen
        # (defined as a constant class variable above) is passed to the show_frame method below, and the
        # respective screen is switched to. Storing a reference to each class in a dictionary like this means
        # that there does not need to be a nested loop in the show_frame method.
        self.screen_dictionary = {
            App.LOGIN_SCREEN: LoginScreen, 
            App.ACCOUNT_LOGIN_SCREEN: AccountLoginScreen,
            App.ACCOUNT_CREATION_SCREEN: AccountCreationScreen,
            App.MAIN_MENU_SCREEN: MainMenuScreen,
            App.BOOK_FLIGHTS_SCREEN: BookFlightsScreen,
            App.VIEW_TICKETS_SCREEN: ViewTicketsScreen,
            App.REMOVE_TICKETS_SCREEN: RemoveTicketsScreen,
            App.FINISH_ORDER_SCREEN: FinishOrderScreen,
            App.ACCOUNT_CREATION_SCREEN_TWO: AccountCreationScreenTwo,
            App.BOOK_FLIGHTS_SCREEN_TWO: BookFlightsScreenTwo
        }

        # Show the login screen frame since this will be what the user
        # should go on once they first start the program.
        self.show_frame(self.LOGIN_SCREEN, None)

    def show_frame(self, frame_index, data_to_pass):
        '''Switch to the specified frame'''
        # The frame_index is where it is specified which screen/frame the program is wishing
        # to switch to, which is done by passing one of the class constants to this method.
        # The data_to_pass is where any data that must be passed to the new frame is put,
        # so that the new frame can access it. For most cases, there is no such data, so this parameter will take the value of: None
    
        # Check whether the screen the program is trying to go to is one that
        # has 'restrictions'/conditions that must be met for the program to go to it
        # (e.g. the user must not have 0 tickets if they want to go to the remove ticket screen).
        # If the program is trying to go to such a screen, check whether the program is able to go to 
        # that screen, and return None if it cannot. Otherwise (if the program can go to the screen),
        # the program will continue executing below.

        # The program checks which screen has been specified by seeing if the frame_index corresponds to
        # one of the constants defined in the App class.
        if frame_index == App.REMOVE_TICKETS_SCREEN:
            # If the user's order is empty, tell them this and do not go to the Remove tickets screen.
            if len(app.user.tickets) == 0:
                messagebox.showinfo("Error", "Your order is empty so you have no tickets to remove.")
                return None                 # Return None so as to exit the method.

        elif frame_index == App.FINISH_ORDER_SCREEN:
            # Start by checking if the user's order is empty, and if so, display a message
            # and do not take them to the Finish order screen.
            if len(app.user.tickets) == 0:
                messagebox.showinfo("Error", "Your order is empty so you cannot finish it.")
                return None         # Return None so that the function stops executing

        # If there are no issues with the user trying to go to the screen which has been specified, the execution
        # will continue below:

        # Check that the current frame is defined before trying to destroy
        # # it (to avoid any unexpected crashes).
        if self.current_frame:
            self.current_frame.destroy()

        # Get the value in the dictionary (which is the class of the new screen) and store it in a new object
        # so that it can be instantiated. This is necessary because the dictionary only stores
        # the class references for each screen, which cannot be instantiated directly.
        FrameClass = self.screen_dictionary.get(frame_index)

        # If the program is switching to a screen that may need data passed to it, then the process to follow here
        # is slighty different because it may be required for some information to be passed via the data_to_pass argument.
        # Regardless of whether this is the case, current_frame will be set equal to the class for the specified
        # screen (FrameClass), and then be instantiated.
        if frame_index == App.ACCOUNT_CREATION_SCREEN or frame_index == App.ACCOUNT_CREATION_SCREEN_TWO:
            # Check if there is any data to pass to the screen. If there is,
            # then it will be the user's name and email address, so pass them as so.
            # Otherwise, pass None as the argument for the user's name and email.
            if data_to_pass != None:
                self.current_frame = FrameClass(self, data_to_pass[0], data_to_pass[1])
            else:
                self.current_frame = FrameClass(self, None, None)

        # For the second booking flights screen, the flight code of the flight the user selected needs
        # to be passed, which is what is done here.
        elif frame_index == App.BOOK_FLIGHTS_SCREEN_TWO:
            self.current_frame = FrameClass(self, data_to_pass)

        # If there is no data that must be passed to the new screen, instantiate the object as normal.
        else:
            # Set the current frame to be the object for the specified screen, and instantiate it.
            self.current_frame = FrameClass(self)

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
        messagebox.showinfo("Farewell", "Have a nice trip!")
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

# Class for the main login screen that the user is brought to when first opening the program.
class LoginScreen(Frame):
    def __init__(self, master):
        '''Class constructor method'''
        super().__init__(master)

        # Set the background colour of the screen.
        self.configure(background = MAIN_BG_COLOUR)

        # Configure the rows and columns to be used in this frame.
        self.columnconfigure((0, 2), weight=2, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure(0, weight=6, uniform='a')
        self.rowconfigure(1, weight=2, uniform='a')
        self.rowconfigure(2, weight=2, uniform='a')
        self.rowconfigure((3, 4, 5), weight=1, uniform='a')

        # Main image which is to be placed at the top of the screen.
        # Used pady = 5 so that there is some space around this image, and that
        # it does not touch the top of the window
        main_image = ImageTk.PhotoImage(Image.open("images/first_screen_image.jpg"))
        main_image_label = Label(self, bg="#ffffff", image=main_image)
        main_image_label.image = main_image
        main_image_label.grid(row = 0, column = 1, pady = 5)

        # Create the main header text label and use the grid method to put it on the screen.
        # The background colour is set to be consistent with the rest of the screen.
        header_lbl = Label(self, text="Welcome to the Flight Booking App!", font=("Arial", 20, "bold"), background = MAIN_BG_COLOUR)
        header_lbl.grid(row=1, column=0, sticky="NESW", columnspan=3)

        # Create the Subtext label and use the grid method to put it on the screen.
        # The background colour is set to be consistent with the rest of the screen.
        subtext_lbl = Label(self, text="What would you like to do?", font=("Arial", 13, "bold"), background = MAIN_BG_COLOUR)
        subtext_lbl.grid(row=2, column=1, sticky="NSWE")

        # Frame which contains the two main buttons (Login and Create Account).
        # This is used so that it is easier to position the buttons on the screen, as they can be treated
        # as one single object on the main screen, which makes it easier to position them.
        # Set the background to MAIN_BG_COLOUR so that this frame has the same
        # background colour as everything else (so that the user cannot see the presence of this frame,
        # and they just see the buttons)
        btn_frame = Frame(self, background = MAIN_BG_COLOUR)
        btn_frame.grid(row = 3, column = 0, columnspan=3, sticky = "NEWS")

        # Configure the row and columns for the button frame
        # There are two buttons and three columns since the column in-between the buttons
        # is used to ensure that the buttons are space out. This middle column should be much
        # smaller than the buttons, and so it has a weight of 1, but the buttons have a weight of
        # 30 which is much larger.
        btn_frame.columnconfigure((0, 2), weight = 30, uniform = 'b')
        btn_frame.columnconfigure(1, weight = 1, uniform = 'b')
        btn_frame.rowconfigure(0, weight = 1, uniform = 'b')

        # Login screen button which goes in the button frame created above, and that
        # takes the user to the screen to login with their account when clicked.
        # Put on the screen using the grid method.
        login_screen_btn = Button(btn_frame, text="Login", width = 15, font = ("bold"), command = lambda: app.show_frame(App.ACCOUNT_LOGIN_SCREEN, None))
        login_screen_btn.grid(row=0, column=0, sticky = "E")

        # Create account button which goes in the button frame created above, and that
        # takes the user to the screen to create an account when clicked.
        # Put on the screen using the grid method.
        create_account_btn = Button(btn_frame, text="Create Account", width = 15, font = ("bold"), command = lambda: app.show_frame(App.ACCOUNT_CREATION_SCREEN, None))
        create_account_btn.grid(row=0, column=2, sticky = "W")

        # Label which goes at the bottom of each screen to store things like 'Back' buttons.
        # However, in this screen, there is nowhere to go 'back' to, so there is no need for
        # a 'Back' button.
        bottom_label = Label(self)
        bottom_label.grid(row = 5, column = 0, columnspan = 3, sticky = "EWS", ipady = 10)

class AccountLoginScreen(Frame):
    def __init__(self, master):
        '''Class constructor method'''
        super().__init__(master)

        # Try to load the json accounts file, and if it does not exist,
        # then create it, and then read from it.

        try:
            with open("accounts.json", "r") as f:
                # If reading from the file is successful (i.e. it exists in the
                # same directory the program was run in), then use the .load()
                # method to parse the accounts data contained.
                self.accounts = json.load(f)
        except:
            # If reading from the file is unsuccessful (i.e. it does NOT exists in the
            # same directory the program was run in), then create the file and write to
            # it the information necessary for it to be used to store user accounts.
            with open("accounts.json", "w") as f:
                json.dump({"accounts": []}, f, indent = 4)

            # Read from the file that has just been created, by using the .load()
            # method to parse the contents of the file.
            with open("accounts.json", "r") as f:
                self.accounts = json.load(f)

        # Set the background colour of the screen.
        self.configure(background = MAIN_BG_COLOUR)

        # Configure the rows and columns to be used in this frame.
        self.columnconfigure((0, 2), weight=2, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1, uniform='a')

        # Create the main header text label and use the grid method to put it on the screen.
        # The background colour is set to be consistent with the rest of the screen.
        header_lbl = Label(self, text="Welcome to the Flight Booking App!", font=("Arial", 20, "bold"), background = MAIN_BG_COLOUR)
        header_lbl.grid(row=0, column=0, sticky="NEWS", columnspan=3)

        # Create a label to tell the user to enter their email, and put it on the screen with the
        # grid method.
        email_lbl = Label(self, text="Please enter your email", font=("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        email_lbl.grid(row=1, column=1, sticky="WENS")

        # Create an entry box on the screen for the user to enter their email address,
        # which is positioned below the label using the grid method.
        self.email_entry = Entry(self)
        self.email_entry.grid(row=2, column=1, sticky="WE")

        # Create a label to tell the user to enter their password, and put it on the screen with the
        # grid method.
        password_lbl = Label(self, text="Please enter your password", font=("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        password_lbl.grid(row=3, column=1, sticky="WENS")

        # Create an entry box on the screen for the user to enter their password,
        # which is positioned below the label using the grid method.
        self.password_entry = Entry(self, show = "*")
        self.password_entry.grid(row=4, column=1, sticky="WE")

        # Used to toggle on/off the password. This is because,
        # if the user clicks the view password button, the program will check whether this variable
        # is True/False, and then use this to determine whether it should change the entry box to show a "*"" character or not.
        self.password_showing = False

        # Button that the user will use to show/hide their password, which is place on the screen
        # to the right of the passowrd entry box using the grid method.
        view_password_btn = Button(self, text = "View", font = ("Arial", 9, "bold"), command = lambda: self.toggle_password())
        view_password_btn.grid(row = 4, column = 2, sticky = "W", padx = 10)

        # Button that the user will click when they have entered all their information and want to login.
        # Put on the screen using the grid method.
        login_btn = Button(self, text="Continue", width = 15, font = ("bold"), command=self.user_login)
        login_btn.grid(row=5, column=1)

        # Label which goes at the bottom of each screen to store things like 'Back' buttons.
        # In this screen, the user can go 'back' to the main menu, so there will be a 'Back' button
        # in this label.
        bottom_label = Label(self)
        bottom_label.grid(row = 6, column = 0, columnspan = 3, sticky = "EWS", ipady = 0)

        # Configure the row/column in the bottom label.
        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')

        # Back button for the user to go back to the main menu screen when clicked.
        # Placed inside the bottom label using the grid method.
        back_btn = Button(bottom_label, text = "Back", font = ("Arial", 9, "bold"), command = lambda:app.show_frame(App.LOGIN_SCREEN, None))
        back_btn.grid(row = 0, column = 0, sticky = "NWS")

    def toggle_password(self):
        '''Toggle the user's password from visible to non-visible and vice versa'''

        # Check whether the password_showing attribute is True/False.
        # If it is True, then it means that the user's password is currently
        # showing on the screen, and so change the entry box to display the text
        # as "*" characters. Otherwise, the user's password is not showing on the screen,
        # so change the password entry box so that it doesn't show "*" characters.
        # Also modify the password_showing attribute once the entry box has been modified.
        if self.password_showing:
            self.password_entry.configure(show = "*")
            self.password_showing = False
        else:
            self.password_entry.configure(show = "")
            self.password_showing = True

    def user_login(self):
        '''Manage the user login part of the program'''

        # Get the email and password the user has entered in the entry boxes,
        # and store them each in their own variable.
        user_email = self.email_entry.get()
        user_password = self.password_entry.get()

        # Start by checking that the user entered an email and a password. If not, display a message and return None
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
        app.show_frame(App.MAIN_MENU_SCREEN, None)

class AccountCreationScreen(Frame):
    def __init__(self, master, user_name, user_email):
        super().__init__(master)

        # Set the background colour and ensure the window is the right size
        self.configure(background = MAIN_BG_COLOUR)
        app.geometry("700x400")

        # Configure the rows and columns to be used in this frame.
        self.columnconfigure((0, 2), weight=2, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure((0, 1), weight=2, uniform='a')
        self.rowconfigure((2, 3, 4, 5, 6, 7), weight=1, uniform='a')

        # Main header text
        header_lbl = Label(self, text="Welcome to the Flight Booking App!", font=("Arial", 20, "bold"), background = MAIN_BG_COLOUR)
        header_lbl.grid(row=0, column=0, sticky="NEWS", columnspan=3)

        sub_header_lbl = Label(self, text = "Please enter the following information", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        sub_header_lbl.grid(row = 1, column = 1, sticky = "EW")

        # Label and entry box for user's name
        name_lbl = Label(self, text = "Name", font = ("Arial", 10, "bold"), background = MAIN_BG_COLOUR)
        name_lbl.grid(row = 2, column = 1, sticky = "NEWS")

        self.name_entry = Entry(self)

        # Check whether a user's name was passed to the method. If so, then insert
        # it into the entry widget.
        if user_name != None:
            self.name_entry.insert(0, user_name)

        self.name_entry.grid(row = 3, column = 1, sticky = "WE")
        
        # Label and entry box for user's email
        email_lbl = Label(self, text = "Email", font = ("Arial", 10, "bold"), background = MAIN_BG_COLOUR)
        email_lbl.grid(row = 4, column = 1, sticky = "NEWS")

        self.email_entry = Entry(self)
        
        # Check whether a user's email was passed to the method. If so, then insert
        # it into the entry widget.
        if user_email != None:
            self.email_entry.insert(0, user_email)

        self.email_entry.grid(row = 5, column = 1, sticky = "WE")
        
        # Button to create account when user has finished entering information
        next_btn = Button(self, text = "Next", width = 15, font = ("bold"), command = self.next_page)
        next_btn.grid(row = 6, column = 1)
        
        # Label which goes at the bottom of each screen to store things like 'Back' buttons
        bottom_label = Label(self)
        bottom_label.grid(row = 7, column = 0, columnspan = 3, sticky = "EWS", ipady = 0)

        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')

        back_btn = Button(bottom_label, text = "Back", font = ("Arial", 9, "bold"), command = lambda:app.show_frame(App.LOGIN_SCREEN, None))
        back_btn.grid(row = 0, column = 0, sticky = "NWS")

    def next_page(self):
        '''Validate the user's input and/or take them to the next screen if they are able to'''

        user_name = self.name_entry.get()
        user_email = self.email_entry.get()

        if len(user_name) == 0 or len(user_email) == 0:
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
        
        app.show_frame(App.ACCOUNT_CREATION_SCREEN_TWO, [user_name, user_email])

class AccountCreationScreenTwo(Frame):
    def __init__(self, master, user_name, user_email):
        super().__init__(master)

        # User's name and email which were gathered from the previous Account creation screen.
        self.user_name = user_name
        self.user_email = user_email
        
        # Set the background colour and ensure the window is the right size
        self.configure(background = MAIN_BG_COLOUR)
        app.geometry("700x450")
        
        # Configure the rows and columns to be used in this frame.
        self.columnconfigure((0, 2), weight=2, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure((0, 1), weight=2, uniform='a')
        self.rowconfigure(2, weight = 3, uniform = 'a')
        self.rowconfigure((3, 4, 5, 6, 7, 8), weight=1, uniform='a')
        
        # Main header text
        header_lbl = Label(self, text="Create an Account", font=("Arial", 20, "bold"), background = MAIN_BG_COLOUR)
        header_lbl.grid(row=0, column=0, sticky="NEWS", columnspan=3)
        
        sub_header_lbl = Label(self, text = "Please choose a password", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        sub_header_lbl.grid(row = 1, column = 1, sticky = "EW")
        
        instructions_lbl = Label(self, text = f"Your Password MUST:\n• Be at least {MIN_PASSWORD_LENGTH} characters long\n• Contain at least one number, symbol,\n and uppercase letter", font = ("Arial", 11, "bold"), justify = "left", background = MAIN_BG_COLOUR)
        instructions_lbl.grid(row = 2, column = 1, sticky = "NEWS")
        
        # Label and entry box for user's name
        name_lbl = Label(self, text = "Password", font = ("Arial", 10, "bold"), background = MAIN_BG_COLOUR)
        name_lbl.grid(row = 3, column = 1, sticky = "NEWS")
        
        self.password_one_entry = Entry(self, show = "*")
        self.password_one_entry.grid(row = 4, column = 1, sticky = "WE")
                
        # Label and entry box for user's email
        password_confirm_lbl = Label(self, text = "Confirm", font = ("Arial", 10, "bold"), background = MAIN_BG_COLOUR)
        password_confirm_lbl.grid(row = 5, column = 1, sticky = "NEWS")
        
        self.password_two_entry = Entry(self, show = "*")
        self.password_two_entry.grid(row = 6, column = 1, sticky = "WE")
        
        # Button to create account when user has finished entering information
        create_account_btn = Button(self, text = "Create Account", width = 15, font = ("bold"), command = lambda:self.user_create_account())
        create_account_btn.grid(row = 7, column = 1)
                
        # Label which goes at the bottom of each screen to store things like 'Back' buttons
        bottom_label = Label(self)
        bottom_label.grid(row = 8, column = 0, columnspan = 3, sticky = "EWS", ipady = 0)
        
        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')
        
        # Used to toggle on/off the password. This is because,
        # if the user clicks the view password button, the program will check whether this variable
        # is True/False and use this to determine whether it should change to show a * character or not.
        self.password_showing = False
        
        view_password_btn = Button(self, text = "View", font = ("Arial", 9, "bold"), command = lambda: self.toggle_password())
        view_password_btn.grid(row = 6, column = 2, sticky = "W", padx = 10)
        
        back_btn = Button(bottom_label, text = "Back", font = ("Arial", 9, "bold"), command = lambda:app.show_frame(App.ACCOUNT_CREATION_SCREEN, [user_name, user_email]))
        back_btn.grid(row = 0, column = 0, sticky = "NWS")
    
    def toggle_password(self):
        '''Toggle the user's password from visible to non-visible and vice versa'''

        if self.password_showing:
            self.password_one_entry.configure(show = "*")
            self.password_two_entry.configure(show = "*")
            self.password_showing = False
        else:
            self.password_one_entry.configure(show = "")
            self.password_two_entry.configure(show = "")
            self.password_showing = True

    def user_create_account(self):
        ''''''
        
        # Get the passwords entered by the user in the entry boxes
        user_password_one = self.password_one_entry.get()
        user_password_two = self.password_two_entry.get()

        # Start by checking that the user did not leave either of the password fields blank.
        # If they did, tell them that they need to enter a password, and return None to exit the
        # method.
        if user_password_one == "" or user_password_two == "":
            messagebox.showinfo("Error", "Please enter a password.")
            return None

        # Check that the user entered the same password in both fields.
        # If they didn't, tell them that the passwords they entered do not match, and return None to exit the
        # method.
        if user_password_one != user_password_two:
            messagebox.showinfo("Error", "The passwords you entered do not match.")
            return None
        
        # Check if the user entered a password too short, and if so, tell them that their password must be
        # at least as long as the minimum password length (which is displayed to them), and then return None
        # to exit the method.
        if len(user_password_one) < MIN_PASSWORD_LENGTH:
            messagebox.showinfo("Error", f"Your password must be at least {MIN_PASSWORD_LENGTH} characters. Please enter a valid password")
            return None
        
        # Check whether the password contains a number by iterating through each character in the password,
        # and setting password_contains_number to True if/when a number is found.
        password_contains_number = False
        for character in user_password_one:
            if character.isnumeric:
                password_contains_number = True

        # If password_contains_number is not True, then there were no numbers found in the user's password.
        # Hence, tell them that their password must contain a number, and then return None to exit the 
        # method.
        if not password_contains_number:
            messagebox.showinfo("Error", "Your password must contain at least one number. Please enter a valid password")
            return None
        
        # Check whether the password contains any uppercase letters by iterating through each character in the password,
        # and setting password_contains_symbol to True if/when there is a character that is not in the alphabet, nor is
        # a number (in such a case, the character must be a symbol).
        password_contains_symbol = False
        for character in user_password_one:
            if not character.isalpha() and not character.isnumeric():
                password_contains_symbol = True

        # If password_contains_symbol is not True, then there were no symbols found in the user's password.
        # Hence, tell them that their password must contain a symbol, and then return None to exit the 
        # method.
        if not password_contains_symbol:
            messagebox.showinfo("Error", "Your password must contain at least one symbol. Please enter a valid password")
            return None
        
        # Check whether the password contains any uppercase letters by iterating through each character in the password,
        # and setting password_contains_uppercase_letter to True if/when an uppercase letter is found.
        password_contains_uppercase_letter = False
        for character in user_password_one:
            if character.isupper():
                password_contains_uppercase_letter = True

        # If password_contains_uppercase_letter is not True, then there were no uppercase letters found in the user's password.
        # Hence, tell them that their password must contain an uppercase letter, and then return None to exit the 
        # method.
        if not password_contains_uppercase_letter:
            messagebox.showinfo("Error", "Your password must contain at least one uppercase letter. Please enter a valid password")
            return None

        self.write_user_to_file(self.user_name, self.user_email, user_password_one)
        # Instantiate the User object and continue to the main part of the program.
        app.user = User(self.user_name, self.user_email)
        app.show_frame(App.MAIN_MENU_SCREEN, None)

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

        app.geometry("400x575")
        # Set the background colour
        self.configure(background = MAIN_BG_COLOUR)

        # Configure the rows and columns to be used in this frame. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 1, uniform = 'a')
        self.columnconfigure(1, weight = 5, uniform = 'a')
        self.rowconfigure(0, weight = 6, uniform = 'a')
        self.rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight = 1, uniform = 'a')

        # Main image which is to be placed at the top of the screen
        # Used pady = 5 so that there is some space around this image, and that
        # it does not touch the top of the window
        main_image = ImageTk.PhotoImage(Image.open("images/main_menu_image.jpg"))
        main_image_label = Label(self, bg="#ffffff", image=main_image)
        main_image_label.image = main_image
        main_image_label.grid(row = 0, column = 1, pady = 5)

        # Labels for the text on the screen
        header_text_lbl = Label(self, text = "Main Menu", font = ("Arial", 20, "bold"), background = MAIN_BG_COLOUR)
        header_text_lbl.grid(row = 1, column = 0, sticky = "NEWS", columnspan = 3)

        subheader_text_lbl = Label(self, text = "What would you like to do?", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        subheader_text_lbl.grid(row = 2, column = 1, sticky = "NEWS")

        # Buttons for each option the user can choose from.
        book_flight_btn = Button(self, text = "Book Flight", font = ("bold"), command = lambda: app.show_frame(App.BOOK_FLIGHTS_SCREEN, None))
        book_flight_btn.grid(row = 3, column = 1, sticky = "WE")

        show_tickets_btn = Button(self, text = "Show Tickets", font = ("bold"), command = lambda: app.show_frame(App.VIEW_TICKETS_SCREEN, None))
        show_tickets_btn.grid(row = 4, column = 1, sticky = "WE")

        remove_ticket_btn = Button(self, text = "Remove ticket from Order", font = ("bold"), command = lambda: app.show_frame(App.REMOVE_TICKETS_SCREEN, None))
        remove_ticket_btn.grid(row = 5, column = 1, sticky = "WE")

        finish_order_btn = Button(self, text = "Finish Order", font = ("bold"), command = lambda: app.show_frame(App.FINISH_ORDER_SCREEN, None))
        finish_order_btn.grid(row = 6, column = 1, sticky = "WE")

        cancel_order_btn = Button(self, text = "Cancel Order", font = ("bold"), command = lambda: app.quit_program())
        cancel_order_btn.grid(row = 7, column = 1, sticky = "WE")
        
        # Label which goes at the bottom of each screen to store things like 'Back' buttons
        bottom_label = Label(self)
        bottom_label.grid(row = 8, column = 0, columnspan = 3, sticky = "EWS", ipady = 5)
        
        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')

class BookFlightsScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        app.geometry("700x400")

        # Set the background colour
        self.configure(background = MAIN_BG_COLOUR)

        # Create the columns and rows as required for everything. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure(0, weight = 3, uniform = 'a')
        self.rowconfigure(1, weight = 13, uniform = 'a')
        self.rowconfigure(2, weight = 2, uniform = 'a')
        self.rowconfigure(3, weight = 2, uniform = 'a')
        self.rowconfigure(4, weight = 2, uniform = 'a')

        header_text_lbl = Label(self, text = "Book a Flight", font=("Arial", 18, "bold"), background = MAIN_BG_COLOUR)
        header_text_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 4)

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
        flight_text_lbl = Label(self, text = "Please select a flight to book it", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        flight_text_lbl.grid(row = 2, column = 0, sticky = "NESW", columnspan = 4)
        
        # Button for when the user is finished entering information into the entry boxes.
        # Note that I had to use lambda in order for the command part of the button
        # to work with passing in inputs to the create_ticket() function.
        continue_btn = Button(self, text = "Continue", font = ("bold"), command = lambda: self.next_page(self.selected_flight_code))
        continue_btn.grid(row = 3, column = 0, columnspan = 4)

        # Label which goes at the bottom of each screen to store things like 'Back' buttons
        bottom_label = Label(self)
        bottom_label.grid(row = 8, column = 0, columnspan = 4, sticky = "EWS", ipady = 0)
        
        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')

        back_btn = Button(bottom_label, text = "Back", font = ("Arial", 9, "bold"), command = lambda:app.show_frame(App.MAIN_MENU_SCREEN, None))
        back_btn.grid(row = 0, column = 0, sticky = "NWS")

    def next_page(self, flight_code):
        '''Get the flight the user has selected and/or take them to the next screen if they have selected a flight'''
        
        # If the user did not select a flight, tell them this, and return None so that
        # the function will stop executing.
        if flight_code == None:
            messagebox.showinfo("Error", "Please select a flight.")
            return None
        
        # If the program execution reaches this point, it means that the user has selected a flight.
        # Thus, take them to the next screen, and pass the flight code of the flight they selected as
        # the data to pass to the new frame.
        app.show_frame(App.BOOK_FLIGHTS_SCREEN_TWO, flight_code)

class BookFlightsScreenTwo(Frame):
    def __init__(self, master, flight_code):
        super().__init__(master)

        self.flight_code = flight_code

        # Set the background colour
        self.configure(background = MAIN_BG_COLOUR)

        self.columnconfigure((0, 2), weight = 1, uniform = 'a')
        self.columnconfigure(1, weight = 3, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 3, uniform = 'a')
        self.rowconfigure((2, 3, 4, 5, 6, 7, 8), weight = 1, uniform = 'a')

        # Determine which flight in the list of all flights that the user has chosen
        for flight in app.ALL_FLIGHTS:
            if flight[FLIGHT_CODE] == flight_code:
                self.chosen_flight = flight      # Store the flight chosen by the user in a new variable (chosen_flight)

        header_text_lbl = Label(self, text = "Book a Flight", font=("Arial", 18, "bold"), background = MAIN_BG_COLOUR)
        header_text_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 4)

        flight_info_lbl = Label(self, text = f"Airline: {self.chosen_flight[FLIGHT_AIRLINE]}\nFlight Code: {self.chosen_flight[FLIGHT_CODE]}\nDestination: {self.chosen_flight[FLIGHT_DEST]}\nDate/Time: {self.chosen_flight[FLIGHT_DEPT]}\nPrice: ${self.chosen_flight[FLIGHT_BASE_PRICE]:.2f}", font = ("Arial", 11, "bold"), justify = "left", background = MAIN_BG_COLOUR)
        flight_info_lbl.grid(row = 1, column = 1, sticky = "NEWS")

        information_text_lbl = Label(self, text = "Please enter the following information about the ticketholder", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        information_text_lbl.grid(row = 2, column = 0, columnspan = 3)

        name_text_lbl = Label(self, text = "Name", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        name_text_lbl.grid(row = 3, column = 1, sticky = "W")

        name_text_entry = Entry(self)
        name_text_entry.grid(row = 4, column = 1, sticky = "EW")
        
        age_text_lbl = Label(self, text = "Age", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        age_text_lbl.grid(row = 5, column = 1, sticky = "W")

        age_text_entry = Entry(self)
        age_text_entry.grid(row = 6, column = 1, sticky = "EW")

        # Button for when the user is finished entering information into the entry boxes.
        # Note that I had to use lambda in order for the command part of the button
        # to work with passing in inputs to the create_ticket() function.
        continue_btn = Button(self, text = "Continue", font = ("bold"), command = lambda: self.create_ticket(age_text_entry.get(), name_text_entry.get()))
        continue_btn.grid(row = 7, column = 0, columnspan = 4)

        # Label which goes at the bottom of each screen to store things like 'Back' buttons
        bottom_label = Label(self)
        bottom_label.grid(row = 8, column = 0, columnspan = 4, sticky = "EWS", ipady = 0)
        
        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')

        back_btn = Button(bottom_label, text = "Back", font = ("Arial", 9, "bold"), command = lambda:app.show_frame(App.BOOK_FLIGHTS_SCREEN, None))
        back_btn.grid(row = 0, column = 0, sticky = "NWS")

    def create_ticket(self, age, holder_name):
        '''Validate information entered by user and instantiate a ticket object'''

        if age == '' or holder_name == '':
            messagebox.showinfo("Error", "Please enter all of the ticketholder's information.")
            return None
        
        if not age.isnumeric():
            messagebox.showinfo("Error", "Please enter a valid age.")
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
        ticket = Ticket(holder_name, self.chosen_flight[FLIGHT_AIRLINE], self.chosen_flight[FLIGHT_CODE], self.chosen_flight[FLIGHT_DEST], self.chosen_flight[FLIGHT_DEST_AIRPORT], self.chosen_flight[FLIGHT_DEST_AIRPORT_CODE], self.chosen_flight[FLIGHT_DEPT], age_type, self.chosen_flight[FLIGHT_BASE_PRICE])
        app.user.add_ticket(ticket)

        # Check if the user's ticket qualified for a discount because of the ticket holder age.
        # If so, display a message to tell the user this, and then display another message as confirmation
        # for their ticket. Even if the user does not qualify for a discount based on their age,
        # still display a confirmation message for their ticket.

        if age_type == "Child":
            messagebox.showinfo("Discount + Confirmation", f"This ticket qualifies for a Child's discount of {(1 - CHILD_TICKET_PRICE) * 100}%, bringing the price down to ${ticket.price:.2f}.\n\nThe Child's ticket has been added to the order.")
        elif age_type == "Senior":
            messagebox.showinfo("Discount + Confirmation", f"This ticket qualifies for a Senior's discount of {(1 - SENIOR_TICKET_PRICE) * 100}%, bringing the price down to ${ticket.price:.2f}.\n\nThe Senior's ticket has been added to the order.")
        else:
            messagebox.showinfo("Confirmation", "The Adult's ticket has been added to the order.")

        # After having created a ticket, the user should return back to the main menu.
        # Thus, remove the booking flight frame with .destroy() and call the main_screen() function.
        app.show_frame(App.MAIN_MENU_SCREEN, None)

class ViewTicketsScreen(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # Set the background colour
        self.configure(background = MAIN_BG_COLOUR)

        app.geometry("700x400")

        # Configure the rows and columns for widgets on this frame. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 10, uniform = 'a')
        self.rowconfigure((2, 3), weight = 1, uniform = 'a')

        header_text_lbl = Label(self, text = "View Tickets", font=("Arial", 18, "bold"), background = MAIN_BG_COLOUR)
        header_text_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 4)

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

        # Label which goes at the bottom of each screen to store things like 'Back' buttons
        bottom_label = Label(self)
        bottom_label.grid(row = 3, column = 0, columnspan = 4, sticky = "EWS", ipady = 0)
        
        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')

        back_btn = Button(bottom_label, text = "Back", font = ("Arial", 9, "bold"), command = lambda:app.show_frame(App.MAIN_MENU_SCREEN, None))
        back_btn.grid(row = 0, column = 0, sticky = "NWS")

class RemoveTicketsScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        app.geometry("700x400")

        # Configure the rows and columns of the ticket removal screen. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 9, uniform = 'a')
        self.rowconfigure((2, 3, 4), weight = 2, uniform = 'a')
        
        # Set the background colour
        self.configure(background = MAIN_BG_COLOUR)
        
        header_text_lbl = Label(self, text = "Remove Tickets", font=("Arial", 18, "bold"), background = MAIN_BG_COLOUR)
        header_text_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 4)

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
        remove_text_lbl = Label(self, text = "Select the ticket you wish to remove", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        remove_text_lbl.grid(row = 2, column = 0, columnspan = 4)

        # Button for when user has entered their ticket number.
        continue_btn = Button(self, text = "Remove", font = ("bold"), command = lambda: self.remove_users_ticket(self.selected_flight_code))
        continue_btn.grid(row = 3, column = 0, columnspan = 4)

        # Label which goes at the bottom of each screen to store things like 'Back' buttons
        bottom_label = Label(self)
        bottom_label.grid(row = 4, column = 0, columnspan = 4, sticky = "EWS", ipady = 0)
        
        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')

        back_btn = Button(bottom_label, text = "Back", font = ("Arial", 9, "bold"), command = lambda:app.show_frame(App.MAIN_MENU_SCREEN, None))
        back_btn.grid(row = 0, column = 0, sticky = "NWS")

    def remove_users_ticket(self, ticket_to_remove):
        '''Remove ticket from order'''
        
        # If the user did not select a flight, tell them this, and return None so that
        # the function will stop executing.
        if ticket_to_remove == None:
            messagebox.showinfo("Error", "Please select a flight.")
            return None
    
        # Remove the ticket specified by the user.
        app.user.remove_ticket(ticket_to_remove)

        # Display a confirmation message to the user that their ticket has been removed.
        messagebox.showinfo("Ticket removed", "Ticket has been removed from your order.")       # Display confirmation to the user.
        
        # Depending on whether the user has any more tickets left, either stay on the remove
        # tickets screen (though calling the show_frame method again to 'refresh' the screen)
        # or exit to the main menu.
        if len(app.user.tickets) != 0:
            app.show_frame(App.REMOVE_TICKETS_SCREEN, None)
        else:
            app.show_frame(App.MAIN_MENU_SCREEN, None)

class FinishOrderScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        app.geometry("700x400")

        self.configure(background = MAIN_BG_COLOUR)

        # Configure the rows and columns for widgets. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure((0, 1), weight = 1, uniform = 'a')
        self.rowconfigure(2, weight = 6, uniform = 'a')
        self.rowconfigure((3, 4, 5), weight = 1, uniform = 'a')

        header_text_lbl = Label(self, text = "Finish Order", font=("Arial", 18, "bold"), background = MAIN_BG_COLOUR)
        header_text_lbl.grid(row = 0, column = 0, sticky = "NEWS", columnspan = 4)

        # Label to display the user's name and email
        user_info_text_lbl = Label(self, text = f"Summary of Order for: {app.user.name} ({app.user.email})", font = ("Arial", 12, "bold"),  background = MAIN_BG_COLOUR)
        user_info_text_lbl.grid(row = 1, column = 0, columnspan = 4)

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
        tree.grid(row=2, column=0, columnspan = 3, sticky='news')

        # Add a scrollbar to the table of tickets
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=3, sticky='nws')

        # Label to display the total price of the user's order
        total_price_lbl = Label(self, text = f"Total Price: ${app.user.calculate_total_price()}", font = ("Arial", 12, "bold"), background = MAIN_BG_COLOUR)
        total_price_lbl.grid(row = 3, column = 1)

        # Button for when the user wants to move on, either to quit the program, or to make another order.
        continue_btn = Button(self, text = "Continue", font = ("bold"), command = lambda:self.continue_command())
        continue_btn.grid(row = 4, column = 1)
        
        # Label which goes at the bottom of each screen to store things like 'Back' buttons
        bottom_label = Label(self)
        bottom_label.grid(row = 5, column = 0, columnspan = 4, sticky = "EWS", ipady = 0)
        
        bottom_label.rowconfigure(0, weight = 1, uniform = 'b')
        bottom_label.columnconfigure(0, weight = 1, uniform = 'b')

        back_btn = Button(bottom_label, text = "Back", font = ("Arial", 9, "bold"), command = lambda:app.show_frame(App.MAIN_MENU_SCREEN, None))
        back_btn.grid(row = 0, column = 0, sticky = "NWS")

    def continue_command(self):
        '''Respond to the user pressing the button'''

        # Write user's ticket information to an external file
        with open("orders.txt", "a") as file:
            file.write(f"\nName: {app.user.name}\n")
            file.write(f"Email: {app.user.email}\n")
            file.write(f"{app.user.display_tickets()}\n")

        # Ask the user whether they want to make another order from a message box.
        response = messagebox.askquestion("Confirmation", "Would you like to make another order?")
        if response == "yes":
            # If the user wants to make another order, remove the finish order frame and take them to the login screen
            # with login_screen().
            app.show_frame(App.LOGIN_SCREEN, None)
        else:
            # If the user does not want to make another order, farewell them.
            app.farewell_user()

# Setup main window
app = App()
app.mainloop()