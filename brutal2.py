import itertools
import random
c=0
tot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
rand = random.sample(list(itertools.permutations(tot,4)),5040)
for i in range(len(rand)):
    c=c+1
    print rand[i] ,c