from math import sin,cos,log

def calc_1(oper,a,b):
    if oper=="+":
        return a+b
    elif oper=="-":
        return a-b
    elif oper=="*":
        return a*b
    elif oper=="/":
        return a/b

def calc_2(oper,a):
    if oper=="sin":
        return sin(a)    
    elif oper=="cos":
        return cos(a)
    elif oper=="log":
        return log(a)
   

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation=input("Enter the operation you want to do(+,-,*,/,sin,cos,log): ")
	
result=calc_1(operation,num1,num2)
print(result)

result=calc_2(operation,num1)      
print(result)
    
    