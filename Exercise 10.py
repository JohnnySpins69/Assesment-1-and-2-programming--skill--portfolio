#Exercise 10: Is it even? - 35 Marks

def checker(number): #made a function named 'checker' that takes one argument/parameter 'number'
    if number % 2 == 0: # Check if the number is divisible by 2 (even/odd)

        return f"Number {number} is Even." #if even, return a message indicating the number is even.

    else: #if not even, return a message indicating the number is odd.
        return f"Number {number} is Odd."

def main(): #made a function named 'main'.
    number = int(input("Enter a number: ")) #added a input for the user to type in.
    
    result = checker(number)  #calls the 'checker' function with the user's number and store the result

    print(result)  #prints the result message returned by the 'checker' function

main() #calls the main function to run the program.

