# Series of 1/1! + 1/2! +1/3! + ......
print("# Series of 1/1! + 1/2! +1/3! + ......")
n=int(input("Enter the end number(denominator) of the series  : "))
sum=0
fac=1
for i in range(1,n+1):
			fac=fac*i
			sum=sum+(1/fac)
print(sum)		
	
			