import numpy as np 
import matplotlib.pyplot as plt 

#   y = 5x+1

# x = np.linspace(-15,15)
x = np.random.uniform(-15,15,50)
y = 5*x + 1
lag = 2

plt.plot(x,y, color='red' ,marker = 'o',label= 'y=5x+1')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.xlim(-15, 15)
plt.ylim(-20, 30)
plt.title(f"Straight line for y = 5x+1")
plt.legend()
# plt.axis('off')
plt.show()