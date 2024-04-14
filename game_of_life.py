import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.animation import FuncAnimation
import random

#non vectorized approach
'''
n=200
li=[list(random.choices([0,1],k=n)) for _ in range(n)]
li[0]=[0]*n
li[-1]=[0]*n
for i in range(n):
    li[i][0]=0
    li[i][-1]=0

for iteration in range(1000):
    li_=[[0]*n for _ in range(n)]
    xs=[]
    ys=[]
    for i in range(1,n-1):
        for j in range(1,n-1):
            s=li[i-1][j]+li[i+1][j]+li[i][j-1]+li[i][j+1]+li[i-1][j-1]+li[i+1][j+1]+li[i+1][j-1]+li[i-1][j+1]
            if li[i][j]:
                if s==2 or s==3:
                    li_[i][j]=1
                    xs.append(i)
                    ys.append(j)
            else:
                if s==3:
                    li_[i][j]=1
                    xs.append(i)
                    ys.append(j)
    li=li_
    if not iteration%1:
        plt.xlim(0,n)
        plt.ylim(0,n)
        plt.scatter(xs,ys,marker='s',color='black')
        plt.pause(0.0001)
        plt.cla()

plt.xlim(0,n)
plt.ylim(0,n)
plt.scatter(xs,ys,marker='s',color='black')

plt.pause(5)
plt.close()
plt.show()

'''
#vectorized approcach

# '''
n=1000
li=np.random.randint(0,2,(n,n), dtype=int)
li[0]=0
li[-1]=0

li[:, 0]=0
li[:, -1]=0


for i in range(1000):
    li_=np.zeros((n,n), dtype=int)
    li_[1:-1,1:-1]=li[1:-1,:-2]+li[1:-1, 2:]+li[:-2,1:-1]+li[2:,1:-1]+li[:-2,:-2]+li[:-2,2:]+li[2:,:-2]+li[2:,2:]
    li_[1:-1,1:-1]=( (li[1:-1,1:-1]==1) & ((li_[1:-1,1:-1]==2)| (li_[1:-1,1:-1]==3)) ) + ( (li[1:-1,1:-1]==0) & (li_[1:-1,1:-1]==3) )
    li=li_

    plt.xlim((0,n-1))
    plt.ylim((0,n-1))

    plt.imshow(~(li), cmap='gray')
    plt.pause(0.01)
    plt.cla()

plt.show()
# '''
# x_values=[]
# y_values=[]

# plt.plot((1,1),(2,2),(5,5))
# plt.show()



# def animate():
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title("Game of Life")

# ani=FuncAnimation(animate,interval=1000, frames=10, repeat=False)


