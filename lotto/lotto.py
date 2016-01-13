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

    def calc_matches(self, pb_number):
        
#        number_element=1
        pb_drawn = pb_number[5]
        pb_number.pop(5)
        line=0
        entry=0
        for row in self.numbers:
            line=line+1
            pb_match=0
            row = [int(i) for i in row]
            pb_ticky = row[5]
            row.pop(5)
#            print pb_ticky
#            print pb_drawn
            if pb_ticky == pb_drawn:
                pb_match=1
#                print "Powerball Number Match ", pb_match
            entry=0
            for i in row:
                entry=entry+1
                for j in pb_number:
                    if i == j:
                        print "Number Match ", line, " ", entry, " (", j, ")" , "PB =", pb_match
                        
            
#            row  = [int(i) for i in row]
#            for x in row:
#                print x
#                for y in pb_number:
#                    if x == y:
#                        print "Match"
#            

tick1 = Ticket(123456, "01/8/2016")

with open('../tickets/2016-01-09.csv', 'rU') as csvfile:
    file_numbers = csv.reader(csvfile)
    for row in file_numbers:
        tick1.add_number(row)



#tick1.display_ticket()
#print "Total Tickets: ", Ticket.ticket_total
#tick1.display_numbers()

pb=[20,1,3,4,5,19]
tick1.calc_matches(pb)


