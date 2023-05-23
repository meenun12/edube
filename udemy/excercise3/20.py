list = [x*x for x in range(5)]
def fun(L):
    del L[L[2]]
    return L

print(fun(list))