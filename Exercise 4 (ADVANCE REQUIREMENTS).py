# Exercise 4: Primitive Quiz - 30 Marks
"""
answer = input ("What is the capital of France?: ")

if answer == "paris":
    print ("Correct")    

else:
    print ("Wrong")

# Exercise 4: Advance Requirement - Bonus point
"""
answer = input("What is the capital of France?: ")
"""
if answer == "paris":
    print ("Correct")     ********************************
elif answer == "Paris":   //not practical and efficient//
    print("Correct")      ********************************
elif answer == "PaRis":
    print ("Correct")
"""
#shortened version = more efficient by making the inputs lower case regardles of how paris is typed

score = 0 #adds a score system to the code

if answer.lower().strip() == "paris": #makes the input automatically made into lower case = .lower() & added .strip() so that the answer is still correct even with space
    print("Correct!") #prints Correct! if the answer is right
    score +=1 #adds 1 point to the score variable
    
else:
    print ("Wrong") #adds else statement if the answer is wrong
    

answer = input ("What is the capital of Germany?: ") #copy and paste & change country
                                                     
if answer.lower().strip() == "berlin": #answer must be berlin
    print("Correct!")
    score +=1 #adds 1 point to the score variable
else:
    print ("Wrong")

answer = input ("What is the capital of Greece?: ") 

if answer.lower().strip() == "athens": #answer must be athens
    print("Correct!") 
    score += 1 #adds 1 point to the score variable
else:
    print ("Wrong")

answer = input ("What is the capital of Portugal?: ")
    
if answer.lower().strip() == "lisbon": #answer must be portugal
    print ("Correct!")
    score += 1 #adds 1 point to the score variable
        
else:
    print ("Wrong")

answer = input ("What is the capital of Italy?: ")

if answer.lower().strip() == "rome": #answer must be rome
    print("Correct!")
    score +=1 #adds 1 point to the score variable

answer = input ("What is the capital of Ireland?:")

if answer.lower().strip() == "dublin": #answer must be dublin
    print("Correct!")
    score += 1 #adds 1 point to the score variable

else:
    print("Wrong")

answer = input ("What is the capital of Belgium?:")

if answer.lower().strip() == "brussels": #answer must be brussels
    print("Correct!")
    score += 1 #adds 1 point to the score variable

else:
    print("Wrong")
    
answer = input ("What is the capital of Sweden?:")

if answer.lower().strip() == "stockholm": #answer must be stockholm
    print("Correct!")
    score += 1 #adds 1 point to the score variable

else:
    print("Wrong")
    
answer = input ("What is the capital of Spain?:")

if answer.lower().strip() == "madrid": #answer must be madrid
    print("Correct!")
    score += 1 #adds 1 point to the score variable

else:
    print("Wrong")
    
answer = input ("What is the capital of Poland?:")

if answer.lower().strip() == "warsaw": #answer must be warsaw
    print("Correct!")
    score += 1 #adds 1 point to the score variable

else:
    print("Wrong")

print ("You scored: ", score, "Out of 10!") #prints the scores acquired
if score >= 5 and score <= 10: #adds an if statement if the score is greater or equal to 6 and score is lower or equal to 10:  |
        print ("You Passed!") #if true = true, prints "You Passed!"                                                                 <-|
else: #adds an else statement to print a fail string if the score < 6
    print ("You Failed, Try again.") #if wrong, prints "You Failed, Try again."


    
