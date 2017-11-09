import random
#
def comp(l1, l2):  # compare random list and user's input
    a = 0  # number and position both OK
    b = 0  # number OK but position not
    c = 0  # numer and position neither not OK
    for i in range(len(l1)):
        if l1[i] in l2:  # check number
            if l1[i] == l2[i]:  # check position
                a = a + 1  # N and P both OK
            else:
                b = b + 1  # N ok but P not
        else:
            c = c + 1  # neither N and P OK
    return [a, b, c]  # return list[a,b,c] and each element is integer


def uin():  # save user input and check its type must be 4 number
    global l1
    uinstate = True
    while uinstate:
        l1 = list(raw_input("Guass number (input 4 different number): "))
        for i in range(len(l1)):
            if l1[i].isdigit() and len(l1) == 4:
                l1[i] = int(l1[i])
                uinstate = False
            else:
                print 'fuck, you should type 4 different number'
                break
    return l1


def ranum():  # generate random 4 numbers
    number_set = []
    for i in range(0, 10, 1):
        number_set.insert(i, i)
    l2 = random.sample(number_set, 4)
    return l2


def brtul(indicator):
    bl = 0
    if indicator:
        bl = bl + 1
    return bl


state = True  # define game on/off state
trail = 0  # count trail times
l2 = ranum()

while state:
    # user input and turn it into int.
    l1 = uin()
    resul = comp(l1, l2)  # compare 2 set
    trail = trail + 1
    print '%dA %dB %dC ,try %d times' % (resul[0], resul[1], resul[2], trail)
    if resul[0] == 4:
        state = False
        print 'Congrate! you find it!'
