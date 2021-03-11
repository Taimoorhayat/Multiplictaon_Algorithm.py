def check_even(a,b):
    l1 = len(str(a))
    l2 = len(str(b))
    a = str(a)
    b = str(b)
    var1,var2 = " "," "

    if l1 % 2 != 0:
               var1 = "0"+a
    else:
        var1 = a
    if l2 % 2 != 0:
               var2 = "0"+b
    else:
        var2 = b
    return [var1,var2]
def second_step(p,q):
    s = check_even(p,q)
    a,b = s[0],s[1]
    v = int(len(str(a))/2)
    h = int(len(str(b))/2)
    m = [a[i:i+v] for i in range(0, len(a), v)]
    n = [b[i:i+h] for i in range(0, len(b), h)]
    return m,n
def multiplication(a,b):
    k = second_step(a,b)
    k1 = k[0]
    k2 = k[1]
    l1,l2 = [],[]
    l1 = [int(i) for i in k1]
    l2 = [int(j) for j in k2]
    l3 = check_even(a,b)
    q = len(l3[0])
    mul1 = (l1[0] * l2[0]) * pow(10,q)
    mul2 = ((l1[0] * l2[1]) + (l1[1]*l2[0]))* pow(10,q/2)
    mul3 = l1[1] * l2[1]
    return int(mul1+mul2+mul3)
    
s = input(int())
t  = input(int())
multiplication(989,7)



