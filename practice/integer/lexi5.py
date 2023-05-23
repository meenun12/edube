A = [ "a" , "b" ,  "c" , "d" ]
B = [ "0" , "1" , "c" , "d" ]
C = [ "a" , "b" , "0" , "1" ]

def solution(A, B, C):
    a = set(A)
    b = set(B)
    c = set(C)

    if c.issubset(a.union(b)):
       for i, val in enumerate(c):
           if val.isdigit():
              if any(x.isalpha for x in c[i+1:]):
                 return False
                 break
              return False
    else:
       return False
