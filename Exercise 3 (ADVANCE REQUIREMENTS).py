#Exercise 3: Biography - 25 Marks
"""
a1 = { "Name":"John Dave D. Palencia",
           "Hometown":"Philippines",
           "Age":20,
}

print(a1["Name"],a1["Hometown"],a1["Age"], sep="\n")
"""
#Advanced Requirements:
"""
"""
name = input("What is your name?: ") #ask the user to input their name.
hometown = input("where is your Hometown?: ") #ask the user to input their hometown.

while True: #made a loop to make sure that the user enters a valid number for age.
    try:
        age = int(input("How old are you?: ")) #ask the user for their age and try to convert it to an integer (age = integer).
        break #exit loop if the while statement is false.
    except ValueError: #if the user enters something that is not a number, show a message and ask again and not have the error message.
        print("Please enter a number")

#stores the user input in the dictionary with keys "Name","Hometown","Age."
my_dict = { "Name": name,
            "Hometown": hometown,
            "Age": age
}

#prints the users info.
print("\nYour Info:")
print("Your name is:", my_dict["Name"])
print("You live in:", my_dict["Hometown"])
print("You are", my_dict["Age"], "years old.")