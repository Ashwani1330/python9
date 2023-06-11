#Function to calculate and display base raised to the power exponent
#Requirements:
    #1. Base and exponets are to be expected as arguements.
    #2. Calculate Base^exponent.
    #3. Return the result (use return statement).
    #4. Display the returned value.

#function definition
def calcpow(number,power):
    result=1
    for i in range(1,power+1):
        result*=number
    return result

#main function
base=int(input("Enter the value for the base: "))
expo=int(input("Enter the value for the exponent: "))

answer=calcpow(base,expo)          #function call
print(base," raised to the power", expo, " is", answer)

# i commited a change.
# yay
