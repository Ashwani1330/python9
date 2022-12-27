def boom(A, B):
    c = []
    for i in A:
        for j in B:
            if i == j:
                c.append(i)

    return c



A = eval(input())
B = eval(input())
print(boom(A, B))
