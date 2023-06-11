a=" "
print(a*10, " PRIME  NUMBER  CHECKER ")
check=1
flag=0
p=int(input("\n Enter a number: "))
while check<= p/2:
	if p%check==0:
		flag=1
	else:                                           #Can also use break statement instead of else
		flag=0
	check=check+1		
if p<1:
	print("\n Number entered is less than 1. Execute again by entering a posetive number,")
elif flag==1:
	print("\n Number entered is not prime.")
else:
	print("\n Entered number is prime.")
