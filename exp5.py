def dq(n):
    if (n==1) or (n==0):
        return 1
    else:
        return dq(n-1) + dq(n-2)

print(dq(38))
