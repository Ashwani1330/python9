def perfect(N):
    facts = factors(N)
    sum = 0
    for i in facts:
        sum += i
    if sum == N:
        return True
    else:
        return False


def factors(N):
    fac = []
    for i in range(1,N//2+1):
        if N % i == 0:
            fac.append(i)
    return fac


N = int(input())
if perfect(N) == True:
    print("Perfect")
else:
    print("Not Perfect")
