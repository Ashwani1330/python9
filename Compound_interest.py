def compound_interest(P, R, T, N):
    CI=((P*(1+(R/N)))**(N*T))
    return CI

Principal=int(input("Enter the principal amount: "))
Rate=int(input("Enter the rate: "))
Time=int(input("Enter the time: "))
Num_of_times=int(input("Enter the number of times: "))

Compound_interest=compound_interest(Principal,Rate,Time,Num_of_times)

print("Compound interest: ",Compound_interest)

      