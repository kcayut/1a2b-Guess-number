a=0
b=0
l1=[5,2,3,4]
l2=[5,2,4,3]
for i in range(len(l1)) :
    if l1[i] in l2:
       if l1[i] == l2 [i]:
           a=a+1
       else:
           b=b+1
repr(a)
repr(b)
print a,b
print (type(a),type(b))
