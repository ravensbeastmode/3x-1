from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import random as rand

num = rand.randint(2,10000)
x= num
timesOne = 0
interval = 0
xAxis = []
yAxis = []
while(x>=1):
    if(x%2==1):
        x = x*3+1
    else:
        x = x/2    
    interval+=1
    if(x==1):
        timesOne+=1
    if(timesOne==10):
        break
    xAxis.append(interval)
    yAxis.append(x)
    print(x)            





style.use('ggplot')

plt.title("Unsolvable Math Problem")

plt.ylabel("Answer")
plt.xlabel("Trial Number")
plt.plot(xAxis,yAxis)
plt.show()