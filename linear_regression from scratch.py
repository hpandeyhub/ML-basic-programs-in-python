import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#y=mx+c is the equation for slop

x=[1,2,3,4,5]
y=[2,4,5,4,5]

mean_x=np.mean(x)
mean_y=np.mean(y)
#print(meany,meanx)
# finding m(slop or coefficient) value

numerator=0
denominator=0
n=len(x)
for i in range(n):
    numerator+=(x[i]-mean_x)*(y[i]-mean_y)
    denominator+=(x[i]-mean_x)**2

m=numerator/denominator
c=mean_y-(m*mean_x)
print("m=",m,"c=",c)

#find y values at any point
val=int(input("enter value x for find y"))
a=(m*val)+c
print(a)

#data ploting
plt.scatter(x,y)
plt.show()
