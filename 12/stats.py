import numpy

n = int(input())
list1 = []

for i in range(n):
    a = int(input())
    list1.append(a)

sum1 = 0
for i in list1:
    sum1 += i

l = len(list1)
mean = sum1/l
print("%.2f" % mean)
ord_list = sorted(list1)

if l%2 != 0:
    median = ord_list[(l+1)//2 - 1]
else:
    median = (ord_list[l//2]+ord_list[l//2+1])/2 - 1

#std_deviation = ()**(1/2)

def variance(ord_list):
    var = 0

    for i in ord_list:
        ele = (i-mean)**2
        var += ele

    varianc1 = var/l
    return varianc1

std_dev = variance(list1)**(1/2)
print("%.2f" % std_dev)
print("%.2f" % median)

x = numpy.std(ord_list)
print("%.2f" % x)
