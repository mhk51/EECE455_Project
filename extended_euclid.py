def extended_euclid(m,b):
    A = [1,0,m]
    B = [0,1,b]
    print(A,B)
    while(not(B[2] == 1) and not ( B[2] == 0)):
        T = B
        Q = A[2]//B[2]
        B = [A[0]-Q*B[0],A[1]-Q*B[1],A[2]-Q*B[2]]
        A = T
        print(A,B)
    if(B[2] == 0):
        print("No inverse")
    elif(B[2] == 1):
        return B[1]+m

print(extended_euclid(26,11))
