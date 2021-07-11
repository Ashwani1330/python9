#String as parameter in function
#Function to display fullname
#Requirements:
    #1. The function should have 2 parameters to accept first name and last name.
    #2. Concatenate name using + operator with a space between first and last name. 
    #3. Display fullname.

#function definition 
def fullname(first,last):
    fullname = first + " " + last
    print("Hello", fullname)
#function ends here

#main function 
first= input("Enter first name: ")
last= input("Enter last name: ")

#function call
fullname(first,last)

