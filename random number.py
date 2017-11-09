import random
list=[]
for i in range(0,10,1):
    list.insert(i,i)
a = random.sample(list,4)
print a,list
