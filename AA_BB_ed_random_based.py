import numpy as np
import random as random
import matplotlib.pyplot as plt

#!!!input number of monomer and the excess amount here!!!
num = 3000
extra = 300

#every monomer has two functionalities
func = [2]* (2*num + extra)
#Alist and Blist labels every functional group in the system
Alist = [0] * 2*num
Blist = [0] * 2*(num + extra)
for i in range(0,2 * num):
    Alist[i] = i
for i in range(0, 2*(num + extra)):
    Blist[i] = i+ 2*num

#conn1 and conn2 take records of how monomers are joined together
conn1 = [-1] * (2*num+extra)
conn2 = [-1] * (2*num+extra)

#randomly pick one A and B functional group, and connect them
#make the reaction go until all A functional groups are consumed

def randList(mylist):
    s = len(mylist)
    nn = random.randint(0, s-1)
    x = mylist[nn]
    mylist.remove(x)
    return x

def reaction(Alist, Blist, num):
    for i in range(0, num):
        p = randList(Alist)
        q = randList(Blist)
        func[p/2] -= 1	
        func[q/2] -= 1
        if func[p/2] == 1:
	    conn1[p/2] = q/2
        if func[p/2] == 0:
	    conn2[p/2] = q/2
        if func[q/2] == 1:
	    conn1[q/2] = p/2
        if func[q/2] == 0:
	    conn2[q/2] = p/2

reaction(Alist, Blist, num)
reaction(Alist, Blist, num)

#This part of code counts how many monomers each polymer contains
#note: recursion of Python has a limit

follow = [1] * (2*num+extra)
unit = [0] * (2*num + extra )
#unit_linear = [0] * (2*num + extra + 1)

chain = [0] * (2*num + extra)

def count_member(follow, conn1, conn2, i):
    global num_count
    global chained
    if follow[i] != 0:
	follow[i] = 0
	num_count += 1
	if (conn1[i] == -1) | (conn2[i] == -1):
	    chained = 1
	if (conn1[i] != -1):
	    count_member(follow, conn1, conn2, conn1[i])  
        if (conn2[i] != -1):
	    count_member(follow, conn1, conn2, conn2[i])

for i in range(0, 2*num + extra):
    chained = 0
    num_count = 0
    count_member(follow, conn1, conn2, i) 
    if num_count != 0:
        unit[num_count] += 1
    if chained == 1:
	chain[num_count] += 1 
     
s1 = sum(unit)
s2 = sum(chain)
print 'overall count:', s1
print 'polymer chain count:', s2

#Result print

plt.subplot(211)
plt.title('overall')
x_axis = [0] * (2*num + extra)
for i in range(0, 2*num + extra):
    x_axis[i] = i
plt.bar(x_axis, unit, color='r')
plt.axis([0, 60, 0, max(unit)+2])

plt.subplot(212)
plt.title('chains')
x__axis = [0] * (2*num +extra)
for i in range(0, 2*num + extra):
    x__axis[i] = i
plt.bar(x__axis, chain, color='b')
plt.axis([0, 60, 0, max(chain)+2])

plt.show()
