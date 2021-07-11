import random
def randomint():
    lucky_int = random.randint(1,600)
    return lucky_int

for i in range(1,601):
    lucky_int=randomint()
    print("Parent", i,"number :", lucky_int)   
    
    
    
    

