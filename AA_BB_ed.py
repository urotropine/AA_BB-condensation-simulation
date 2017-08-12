import numpy as np
from random import random
import matplotlib.pyplot as plt
from math import sqrt

num = 1000
extra = 10

dots__x = [0]*( 2*num+extra)
dots__y = [0]*( 2*num+extra)
func = [2]* num
next = [0]* num
for i in range(0, num):
    next[i] = i

#dots_B_x = [0] * (num + extra)
#dots_B_y = [0] * (num + extra)
func_B = [2] * (num + extra)

conn1 = [-1] * (2*num+extra)
conn2 = [-1] * (2*num+extra)

#print next
#print func
#print conn1
#print conn2

for i in range(0,num):   
    dots__x[i] = random()
    dots__y[i] = random()

for i in range(num,2*num+extra):
    dots__x[i] = random()
    dots__y[i] = random()

def reaction(num, dots__x, dots__y, func, next, extra,  func_B):
    for i in range(0, num):
        end = i
        if func[i] > 0:
	    p = 2
	    for j in range(num,2*num + extra):
	        if((next[i]!=j) & (func_B[j-num] > 0)):
		    dx = dots__x[j] - dots__x[i]
		    dy = dots__y[j] - dots__y[i]
		    m = sqrt(dx*dx + dy*dy)
		    if p > m:
		        p = m
		        end = j
	    func_B[end-num] -= 1
	    func[i] -= 1	
	    next[i] = end
	    if func[i] == 1:
		conn1[i] = end
	    if func[i] == 0:
		conn2[i] = end
	    if func_B[end-num] == 1:
		conn1[end] = i
	    if func_B[end-num] == 0:
		conn2[end] = i
	    plt.plot([dots__x[i], dots__x[end]], [dots__y[i], dots__y[end]])	

plt.subplot(211)
reaction(num, dots__x, dots__y, func, next, extra,  func_B)
reaction(num, dots__x, dots__y, func, next, extra,  func_B)

follow = [1] * (2*num+extra)
unit = [0] * (2*num + extra )
#unit_linear = [0] * (2*num + extra + 1)
linear = 0

def count_member(follow, conn1, conn2, i):
    global num_count
    if follow[i] != 0:
	follow[i] = 0
	num_count += 1
	if (conn1[i] != -1):
	    count_member(follow, conn1, conn2, conn1[i])  
        if (conn2[i] != -1):
	    count_member(follow, conn1, conn2, conn2[i])

for i in range(0, 2*num + extra):
    num_count = 0
    count_member(follow, conn1, conn2, i) 
    if num_count != 0:
        unit[num_count] += 1      

#print next
#print func
#print func_B
#print conn1
#print conn2

#print unit

dots_A_x = [0] * num
dots_A_y = [0] * num
dots_B_x = [0] * (num + extra)
dots_B_y = [0] * (num + extra)
for i in range(0, num):
    dots_A_x[i] = dots__x[i]
    dots_A_y[i] = dots__y[i]
for i in range(num,2*num+extra):
    dots_B_x[i-num] = dots__x[i]
    dots_B_y[i-num] = dots__y[i]
plt.plot(dots_A_x, dots_A_y, 'ro')
plt.plot(dots_B_x, dots_B_y, 'bs')
plt.axis([0,1,0,1])

plt.subplot(212)
x_axis = [0] * (2*num + extra)
for i in range(0, 2*num + extra):
    x_axis[i] = i
plt.bar(x_axis, unit, color='r')
plt.axis([0, 300, 0, max(unit)+2])

plt.show()
