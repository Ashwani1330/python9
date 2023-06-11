#Program to calculate factorial using user defined function calcFact()
#number num as an arguement
#Requirements are listed below:
    #1. The function should accept one integer arguement from the user.
    #2. Calulate factorial.
    #3. Display factorial.

#function definition
def calcFact(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    print("Factorial of",num,"is",fact)

#main function
num= int(input("Enter the number: "))

#function call
calcFact(num)
