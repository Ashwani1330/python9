# Number of days in the month entered by the user
# All keys in alphabetical order 
# All months with 31 days  
# Key value pairs sorted by the days in the month   
dict1={'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
month=str(input("Enter the name of the month: "))
for key in dict1:
	key=month
	value=dict1[key]
print("\n Number of days in the month is : ", value)

