import random

state = True
trail = 0

# generate random 4 numbers
rl = []
for i in range(0, 10, 1):
    rl.insert(i, i)
l2 = random.sample(rl, 4)  # from the rl, pick 4 number to form a list
print l2

#

while state:  # determine the current state
    # userinput and turn it into integer.
    l1 = list(raw_input("Guass number "))
    for i in range(len(l1)):
        l1[i] = int(l1[i])
        #

    # compare 2 set
    a = 0  # initial A and B
    b = 0
    c = 0

    for i in range(len(l1)):  # check out whether the user input is in the guesses list
        if l1[i] in l2:  # if in it, is the position correct
            if l1[i] == l2[i]:  # if position correct A=A+1
                a = a + 1
            else:  # if not B=B+1
                b = b + 1
        else:  # if not in l2, c=c+1
            c = c + 1

    trail = trail + 1
    print '%dA %dB %dC,try %d times' % (a, b, c, trail)

    if a == 4:
        state = 0
        print "Correct, Congratulation!"
        #
