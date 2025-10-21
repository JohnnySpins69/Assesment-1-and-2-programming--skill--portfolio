#Exercise 8: Simple Search - 30 Marks

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #lists of names.

name_search = input("Who are you trying to find?: ").capitalize().strip() #asks the the user for input/used .capitalize and .strip to be more user friendly.

if name_search in names: #if the input typed is in names, prints the input is in the list.
    print(name_search,"is in the list.")

else: #if not, prints input is not in the list.
    print(name_search,"is not in the list.")

