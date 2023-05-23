A = [ "a" , "b" ,  "c" , "d" ]
B = [ "0" , "1" , "c" , "d" ]
C = [ "a" , "b" , "0" , "1" ]

def solution(A, B, C):
    a_set = set(A)
    b_set = set(B)
    c_set = set(C)

    # Check if all elements of C are present in A or B
    if c_set.issubset(a_set.union(b_set)):
        # Check if there are no numbers before letters in C
        for i, val in enumerate(C):
            if val.isdigit():
                if any(x.isalpha() for x in C[i+1:]):
                    return False
                break
        return True
    else:
        return False
