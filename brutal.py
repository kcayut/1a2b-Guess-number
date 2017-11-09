import random

tot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
already = []
alreadyro = []
state = True
state2 = True
count = 0
count2 = 0

while state == True:
    rl = sorted(random.sample(tot, 4))
    if rl in already:
        pass
    else:
        already.append(rl)
        rlro = random.sample(rl, 4)
        alreadyro.append(rlro)
        state2 = True
        while state2 == True:
            if rlro in alreadyro:
                count2 = count2 + 1
                if count2 >= 12:
                    state2 = False
                else:
                    rlro = random.sample(rl, 4)
                    alreadyro.append(rlro)
                    c = rl in already
                    d = rlro in alreadyro
                    count = count + 1
                    print rl, rlro, count, count2

