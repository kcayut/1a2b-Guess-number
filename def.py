import random
def t1(a,b):
    return a+b,a-b
def t2(a,b):
    return a*b

def l2():
    rl=[]
    for i in range(0,10,1):
        rl.insert(i,i)
    l2 = random.sample(rl,4)
    return l2


print t1(2,3),t2(5,6),l2()
