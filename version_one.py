# Date: 19/07/2024
# Author: Joshua Hutchings
# Version: 1
# Purpose: Create a program that allows the user to book a plane flight

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
        pass

class Ticket:
    def __init__(self, airline, flight_code, destination_airport, age_type):
        self.airline = airline
        self.flight_code = flight_code
        self.destination_airport = destination_airport
        self.age_type = age_type
        self.discount_amount = 0.0

    def calculate_price(self):
        '''Calculate price on ticket from base price for flight, as well as other factors'''
        pass

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