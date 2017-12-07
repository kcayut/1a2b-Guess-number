import random

#
def compare(l1, l2):  # compare random list and user's input
    a = 0  # number and position both OK
    b = 0  # number OK but position not
    c = 0  # numer and position neither not OK
    for i in xrange(len(l1)):
        if l1[i] in l2:  # check number
            if l1[i] == l2[i]:  # check position
                a = a + 1  # N and P both OK
            else:
                b = b + 1  # N ok but P not
        else:
            c = c + 1  # neither N and P OK
    return [a, b, c]  # return list[a,b,c] and each element is integer


def Normalizelist(l1):
    for i in xrange(len(l1)):
        if l1[i].isdigit() and len(l1) == 4 and len(set(l1)) == 4:
            l1[i] = int(l1[i])
        else:
            print 'fuck, you should type 4 different number'
            return None
    return l1


def userinput():  # save user input and check its type must be 4 number
    state = True
    while state:
        l1 = list(raw_input("Make a Guass (input 4 different number): "))
        l1 = Normalizelist(l1)
        if l1 is None:
            state = True
        else:
            return l1

def Guserinput():
    state = True
    while state:
        l1 = list(raw_input("Input 4 different number to make computer gauss: (input 4 different number): "))
        l1 = Normalizelist(l1)
        if l1 is None:
            state = True
        else:
            return l1

def modechecker(mode):
    while not mode.isdigit():
        mode = raw_input('Pleas input an integer, try again')
    mode = int(mode)
    return mode


def randtobegaussed():  # generate random 4 numbers
    number_set = []
    for i in xrange(0, 10, 1):
        number_set.insert(i, i)
    l2 = random.sample(number_set, 4)
    return l2


def brtul():
    import itertools
    tot = [x for x in range(10)]
    rand = random.sample(list(itertools.permutations(tot, 4)), 5040)
    for i in range(len(rand)):
        rand[i] = list(rand[i])
    return rand


mode = raw_input('Chose mode: 1.player guass 2.computer gauss (type an integer and press Enter)')
mode = modechecker(mode)
if mode == 1:
    state = True  # define game on/off state
    trail = 0  # count trail times
    listTBG = randtobegaussed()
    while state:
        # user input and turn it into int.
        l1 = userinput()
        resul = compare(l1, listTBG)  # compare 2 set
        trail = trail + 1
        print '%dA %dB %dC ,try %d times' % (resul[0], resul[1], resul[2], trail)
        if resul[0] == 4:
            state = False
            print 'Congrate! you find it!'
elif mode == 2:
    mode = raw_input('Chose mode: 1.brtual force (random gauss) 2.others (type an integer and press Enter)')
    mode = modechecker(mode)
    if mode == 1:
        listTBG = Guserinput()
        trail = 0
        l = brtul()
        for i in range(len(l)):
            resul = compare(listTBG, l[i])
            if resul[0] == 4:
                trail = trail + 1
                print 'Finally find it! the answer is ' + str(l[i]) + ' ,and try %d times' % (trail)
                break
            else:
                trail = trail + 1
                print str(l[i]) + ', %dA %dB %dC ,try %d times' % (resul[0], resul[1], resul[2], trail)
    elif mode == 2:
        print 'Not complete yet, end of the program.'
    else:
        print 'Not define, end of the program.'
        pass

else:
    print 'Not define, end of the program.'
