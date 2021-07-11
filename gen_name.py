def gen_name(name,gender):
    if gender=="M":
        print("Mr", name)
    elif gender=="F":
        print("Ms", name)
    else: 
        print("Error! Please RE-execute the program.")

name=input("Enter your name: ")
gender=input("Enter you gender(M for male & F for female): ")

gen_name(name,gender)

