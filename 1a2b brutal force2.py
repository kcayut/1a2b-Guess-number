import random
trail=0
state=True
trial = 0
if state == True:
    rl=[]
    for x in range(0,10,1):
        rl.insert(x,x)
    l2 = random.sample(rl,4)

    tl=[0,0,0,0]
    for i in range(0,10,1):
        tl[0]=i
        for j in range(0,10,1):
            tl[1]=j
            for k in range(0,10,1):
                tl[2]=k
                for l in range(0,10,1):
                    tl[3]=l
                    print tl
                    a=0
                    b=0
                    c=0
                    for m in range(len(tl)):
                        if tl[m] in l2:
                            if tl[m]==l2[m]:
                                a=a+1
                            else:
                                b=b+1
                        else:
                            c=c+1
                    trial = trial+1
                    print (a,b,c,trial )
                    
                    if a==4:
                        state=False
                        print 'Yessssss'

                
