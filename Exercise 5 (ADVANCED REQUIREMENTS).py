#Exercise 5: Days of the Month - 30 Marks

month_dict =  { 
    1: ("January", 31),
    2: ("February", 28),
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30), #dictionary of months and days.
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

month_num =int(input("Select a month number (1-12): ")) #input to ask the user to select a month number (1-12).

if month_num in month_dict: #checks if the month number entered by the user is valid (exists in the dictionary).
    name, days = month_dict[month_num] #gets the month name and number of days from the dictionary.

#leap year section
if month_num == 2: 
    leap = input("Is it a leap year? (Yes/No): ").lower().strip() #asks user if it is a leap year.
    if leap == "yes": #if it is a leap year, updates the number of days to 29.
        days = 29

    print(name,"has",days,"days.") #prints the result showing the month name and number of days
    
else: #if the month number is not valid, print "Invalid month number."
    print("Invalid month number.")
    
