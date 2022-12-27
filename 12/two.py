def str_chk(str1):
    l = str1.split(' ')
    spaces = len(l) - 1
    lower = 0
    upper = 0
    for i in l:
        for j in i:
            if j.isupper() == True:
                upper += 1
            elif j.islower() == True:
                lower += 1
    tup = (upper, lower, spaces)
    return tup

str2 = input()
a = str_chk(str2)
for i in a:
    print(i)

for i in range(12):
    print(12)
