def comp(l1,l2):
    a=0
    b=0
    c=0
    for i in range(len(l1)):
        if l1[i] in l2:
            if l1[i]==l2[i]:
                a=a+1
            else:
                b=b+1
        else:
            c=c+1
    resul=[a,b,c]
    return resul

l1=[1,2,3,4]
l2=[5,6,7,8]
r =comp(l1,l2)
print '%dA%dB%dC'% (r[0],r[1],r[2])
print r
