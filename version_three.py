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

    user = None

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
        self.frames.append(BookFlightsScreen(self))
        self.frames.append(ViewTicketsScreen(self))
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
        #global user

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
        app.user = User(user_name, user_email)

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

        # Columns for table of flights
        column = ("Airline", "Code", "Destination", "Date/Time", "Price")

        # Create a Treeview widget for the table
        tree = ttk.Treeview(self, columns = column, show = "headings")

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
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky='nws')

        # Below are the labels for all of the text on this frame, as well as the entry boxes for user input.
        flight_text_lbl = Label(self, text = "Flight Code:", font = ("Arial", 10))
        flight_text_lbl.grid(row = 2, column = 1, sticky = "W")

        flight_text_entry = Entry(self)
        flight_text_entry.grid(row = 2, column = 1)

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
        continue_btn = Button(self, text = "Continue", command = lambda: self.create_ticket(flight_text_entry.get(), age_text_entry.get(), name_text_entry.get()))
        continue_btn.grid(row = 5, column = 1)

    def create_ticket(self, flight_code, age, holder_name):
        '''Validate information entered by user and instantiate a ticket object'''

        # Used when checking that user has entered the code for a flight that exists
        flight_exists = False

        # Check the flight code entered by the user with the flight code of each
        # available flight. This is to make sure that the flight code entered by
        # the user corresponds to an actual flight that exists.
        for flight in ALL_FLIGHTS:
            if flight[FLIGHT_CODE] == flight_code:
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
        ticket = Ticket(holder_name, chosen_flight[FLIGHT_AIRLINE], chosen_flight[FLIGHT_CODE], chosen_flight[FLIGHT_DEST], chosen_flight[FLIGHT_DEST_AIRPORT], chosen_flight[FLIGHT_DEST_AIRPORT_CODE], chosen_flight[FLIGHT_DEPT], age_type, chosen_flight[FLIGHT_BASE_PRICE])
        app.user.add_ticket(ticket)

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
        app.show_frame(App.MAIN_MENU_SCREEN)

class ViewTicketsScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the rows and columns for widgets on this frame. Doing this manually means that I can
        # adjust the relative sizes of each column/row (from setting the weight). It also means that I can
        # fix the uniformity problem that arises with the grid method.
        self.columnconfigure((0, 2), weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 7, uniform = 'a')
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 10, uniform = 'a')
        self.rowconfigure((2, 3, 4, 5), weight = 1, uniform = 'a')

        # Columns for table of tickets
        column = ("#", "Name", "Airline", "Code", "Destination", "Type", "Date/Time", "Price")

        # Create a Treeview widget for the table
        tree = ttk.Treeview(self, columns = column, show = "headings")

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
        for i in range(len(app.user.tickets)):
            data.append((f"{i + 1}", f"{app.user.tickets[i].holder_name}", f"{app.user.tickets[i].airline}", f"{app.user.tickets[i].flight_code}", f"{app.user.tickets[i].destination}", f"{app.user.tickets[i].age_type}", f"{app.user.tickets[i].estimated_departure}", f"${app.user.tickets[i].price:.2f}"))

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

# Setup main window
app = App()
app.mainloop()