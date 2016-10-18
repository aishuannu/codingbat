def front3(a):
    b = len(a) - 1
    if b < 2:
       return a[0: ] * 3
    else:
       c = a[0]+a[1]+a[2] 
       return c * 3

    
