#!/usr/bin/python

# Created on Jan 10, 2016


import csv


class Ticket:

    ticket_total = 0

    def __init__(self, ticket_number, purch_date):
        self.tick_number = ticket_number
        self.date = purch_date
        self.numbers= []
        Ticket.ticket_total += 1

    def display_ticket(self):
        print "Ticket Number: ", self.tick_number 
        print "Purchase Date: ", self.date 
    
    def add_number(self, tnumber):
        self.numbers.append(tnumber)
    
    def display_numbers(self):
        for row in self.numbers:
            print(row)



tick1 = Ticket(123456, "01/8/2016")

with open('../tickets/2016-01-09.csv', 'rU') as csvfile:
    file_numbers = csv.reader(csvfile)
    for row in file_numbers:
        tick1.add_number(row)



tick1.display_ticket()
print "Total Tickets: ", Ticket.ticket_total
tick1.display_numbers()
