import numpy as np
import matplotlib.pyplot as plt
import random, time, math

# Part c
def flip_coins(flips,p):
    myFlips = np.random.choice(2,flips,p=[(1-p),p])
    return sum(myFlips)
fig1 = plt.figure(1)
for flips, i in zip([10,100,1000,4000], range(1,5)):
    fig1.add_subplot(2,2,i)
    heads = flip_coins(flips,.7)
    plt.bar([0,1],[flips-heads,heads])
    plt.title("Part c: k=%d"% flips)
    plt.xlabel("[Tails, Heads]")
    plt.ylabel("Number of Heads or Tails")
plt.tight_layout()
plt.show()

# Part d

def runs(flips):
    RUNS = 1000
    return [flip_coins(flips,.7) for _ in range(RUNS)]
fig2 = plt.figure(2)
for flips, i in zip([10,100,4000], range(1,4)):
    fig2.add_subplot(3,1,i)
    plt.hist(runs(flips))
    plt.title("Part d: k=%d" % flips)
    plt.xlabel("Number of Heads for Run")
    plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Part e
def plot_fractions(flips, p):
    m = 1000
    myFlips = [flip_coins(k,.7)/k for k in range(1,flips+1)]
    return myFlips
fig3 = plt.figure(3)
for flips, i in zip([10,100,4000], range(1,4)):
    fig3.add_subplot(3,1,i)
    plt.plot(plot_fractions(flips, .7))
    plt.title("Part e: k=%d" % flips)
    plt.xlabel("Number of Heads for Run")
    plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Part f
##plt.figure(4)
def q_curve_norm(k,p):
    RUNS = 1000
    def head():
        norm_heads = flip_coins(k,p) / float(k)
        norm_heads = p + (norm_heads - p) * math.sqrt(k)
        return norm_heads
    heads = [head() for _ in range(RUNS)]
    heads.sort()
    plt.plot(heads, list(range(1, RUNS + 1)))

for k in [10, 50, 100, 500, 2000]:
    q_curve_norm(k,.7)
plt.title("Part f: Normalized Plot")
plt.xlabel("All Tails to All Heads")
plt.ylabel("Number of Trials")
plt.show()

# Part g
def hist_norm(k,p):
    RUNS = 1000
    return [(flip_coins(k,p)-(k*p))/math.sqrt(k) for _ in range(RUNS)]
fig5 = plt.figure(5)
for flips, i in zip([10,100,1000,4000], range(1,5)):
    fig5.add_subplot(2,2,i)
    plt.hist(hist_norm(flips,.7))
    plt.title("Part g: Normalized, k=%d" % flips)
plt.tight_layout()
plt.show()

#Part h
fig6 = plt.figure(6)
fig6.add_subplot(3,2,1)
for p, i in zip([.9,.6,.5,.4,.3],range(1,6)):
    fig6.add_subplot(3,2,i)
    for k in [10, 50, 100, 500, 2000]:
        q_curve_norm(k,p)
        plt.title("Part h: p=%s" % str(p))
plt.tight_layout()
plt.show()
fig7 = plt.figure(7)
for flips, i in zip([10,100,1000,4000], range(1,5)):
    fig7.add_subplot(2,2,i)
    plt.hist(hist_norm(flips,.9))
    plt.title("Part h: Normalized, k=%d p=.9" % flips)
plt.tight_layout()
plt.show()
fig8 = plt.figure(8)
for flips, i in zip([10,100,1000,4000], range(1,5)):
    fig8.add_subplot(2,2,i)
    plt.hist(hist_norm(flips,.6))
    plt.title("Part h: Normalized, k=%d p=.6" % flips)
plt.tight_layout()
plt.show()
fig9 = plt.figure(9)
for flips, i in zip([10,100,1000,4000], range(1,5)):
    fig9.add_subplot(2,2,i)
    plt.hist(hist_norm(flips,.5))
    plt.title("Part h: Normalized, k=%d p=.5" % flips)
plt.tight_layout()
plt.show()
fig10 = plt.figure(10)
for flips, i in zip([10,100,1000,4000], range(1,5)):
    fig10.add_subplot(2,2,i)
    plt.hist(hist_norm(flips,.4))
    plt.title("Part h: Normalized, k=%d p=.4" % flips)
plt.tight_layout()
plt.show()
fig11 = plt.figure(11)
for flips, i in zip([10,100,1000,4000], range(1,5)):
    fig11.add_subplot(2,2,i)
    plt.hist(hist_norm(flips,.3))
    plt.title("Part h: Normalized, k=%d p=.3" % flips)
plt.tight_layout()
plt.show()

# Part i



