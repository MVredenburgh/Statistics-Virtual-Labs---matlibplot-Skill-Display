import numpy as np
import matplotlib.pyplot as plt
def flip_coins(flips,p):
    myFlips = np.random.choice(2,flips,p=[(1-p),p])
    return sum(myFlips)
fig = plt.figure(1)
for flips, i in zip([10,100,1000,4000], range(1,5)):
    print(i,flips)
    fig.add_subplot(2,2,i)
    heads = flip_coins(flips,.7)
    plt.bar([0,1],[flips-heads,heads])
    plt.title("Part c: k=%d"% flips)
    plt.xlabel("[Tails, Heads]")
    plt.ylabel("Number of Heads or Tails")
plt.tight_layout()
plt.show()
