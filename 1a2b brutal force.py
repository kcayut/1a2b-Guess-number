
import random
state = True
trail=0
tl=[0,0,0,0]

#generate random 4 numbers
rl=[]
for i in range(0,10,1):
    rl.insert(i,i)
l2 = random.sample(rl,4)
#

while state:
    

    # compare 2 set 
    a=0 # initial A and B
    b=0
    c=0
    for i in range(0,10,1):
        tl[0]=i
        for j in range(0,10,1):
            tl[1]=j
            for t in range(0,10,1):
                tl[2]=t
                for e in range(0,10,1):
                    tl[3]=e
                    print tl
                    for i in range(len(tl)) : #wheter the user input is in there
                           if tl[i] in l2: #if in it, is the position correct
                               if tl[i] == l2 [i]: # if position correct A=A+1
                                   a=a+1
                               else: # if not B=B+1
                                   b=b+1
                              else: # if not in l2, c=c+1
                                    c=c+1
                



    trail=trail+1 
    print '%dA %dB %dC,try %d times' %(a,b,c,trail)

    if a==4:
        state=0
        print "Correct, Congratulation!"
    #
