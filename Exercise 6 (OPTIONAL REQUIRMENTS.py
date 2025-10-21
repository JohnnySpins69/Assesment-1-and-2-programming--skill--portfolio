#Exercise 6: Brute Force Attack - 30 Marks + Optional Requirements

correct_password = "12345" #adds a variable with the correct password inside.
attempts = 0 #sets the attemps at 0 (Counter).
max_attempts = 5 #adds a limit at how many attempts can be used in entering the password.
attempts_remaining = 5 #the remaining attempts on guessing the password.

while attempts < max_attempts: #added a while loop that keeps on asking as long as its within the max attempts.
    password = input("Enter your password:") #set an input for the user for the password, converts the input into an integer.
    
    if password == correct_password: #adds an if condition that checks if the input password matches the correct password.
        print ("Signed in, Welcome!") #if true prints "Signed in, Welcome!"
        break #breaks the loop if the if statement is true.
        
    else: #adds an else function if the if statement is false
        print ("Wrong password, please try again") #prints "Wrong password, please try again" if the user fails to type the correct password.
        attempts += 1 #adds an extra 1 to the counter whenever the user inputs the wrong password.
        attempts_remaining -= 1 #Decreases the number of remaining attempts by 1.
        print ("You have", attempts_remaining, "Left") #displays how many attempts the user has left.

if attempts == max_attempts: #checks if the user has used up all their attempts.
    print ("Too many attempts, Try again later") #tells when the user exceeded the maximum attempts.
