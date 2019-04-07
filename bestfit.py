from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import random

x = np.array([60,40,70,50,60,80,50,90,40,60])
y = np.array([30,25,60,45,50,45,20,55,30,35])

line=[]

def best_fit(x,y):
	slope = (mean(x)*mean(y)-mean(x*y))/(mean(x)*mean(x)-mean(x*x))
	intercept = mean(y)-slope*mean(x)
	return slope,intercept

m,b=best_fit(x,y)

def squared_error(y_orig,y_line):
	return sum((y_orig-y_line)**2)

def R_sqaured(y_orig,y_line):

	y_mean_line = [mean(y_orig) for y in y_orig]
	squared_error_reg=squared_error(y_orig,y_line)
	squared_error_mean=squared_error(y_orig,y_mean_line)
	return (squared_error_reg/squared_error_mean)

for i in x:
	line.append((m*i)+b)
print(m,b)


# pr_x=8
# pr_y=m*pr_x+b
# plt.scatter(pr_x,pr_y)

plt.scatter(x,y)
plt.plot(x,line)

R_sqaured_value = R_sqaured(y,line)
print(R_sqaured_value)
plt.show()