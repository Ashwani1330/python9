# 2strings + 2complexno. + 2 integers
# 1: Integer is prime
# 2: String is palindrome
# 3: Both 1 & 2
# 4: None of 1 & 2
# 5: Invalid input

list1 = eval(input())
list2 = []

def prime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
        else:
            pass
    return True        
    
test1 = 0
test2 = 0

def com(num):
    real = num.real
    imag = num.imag
    return complex(imag, real)

def comp(num):
    real = num.real
    imag = num.imag
    return complex(real, -imag)


for i in list1:
    if type(i) == int:
        if prime(i) == True:
            test1 = 1
    if type(i) == str:
        if i == i[::-1]:
            test2 = 1

str1 = ''

# Test 1
if test1 == 1 and test2 == 0:
    for i in list1:
        if type(i) == str:
            str1 = i[::-1]
            index = list1.index(i)
            list2.insert(index, str1)
        if type(i) == int:
            index = list1.index(i)
            list2.insert(index, i)
        if type(i) == complex:
            j = com(i)
            index = list1.index(i)
            list2.insert(index, j)

# Test 2
if test1 == 0 and test2 == 1:
    for i in list1:
        if type(i) == int:
            j = -i
            index = list1.index(i)
            list2.insert(index, j)
        if type(i) == str:
            index = list1.index(i)
            list2.insert(index, i)
        if type(i) == complex:
            j = comp(i)
            index = list1.index(i)
            list2.insert(index, j)


# Test 3
if test1 == 1 and test2 == 1:
   print(list1[len(list1)//2]) 
   exit()

# Test 4
if test1 == 0 and test2 == 0:
    for i in list1:
        if type(i) == int:
            list2.append(i)
        if type(i) == complex:
            list2.append(i)
        if type(i) == str:
            str1 = list(i)
            list2 = list2 + str1

# Test 5
if len(list1) < 3 or len(list1) > 6:
    print("Invalid Data")
    exit()


print(list2)
