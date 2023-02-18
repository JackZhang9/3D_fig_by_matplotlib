import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



# x=np.arange(5)
# y=np.arange(1,6)
# coord=np.meshgrid(x,y)
# print(coord)

def f(x1,x2):
    # return 3.5*(np.cos(x1)+np.sin(x2))**2-x1*x2
    # return np.sin(x1)+np.cos(x2)
    return x1**2+x1*2+x2*3+2*x2**2

X1=np.arange(-10,10,0.5)
X2=np.arange(-10,10,0.5)
# print(X1.shape,X1.size)
X1,X2=np.meshgrid(X1,X2)
# print(X1.shape,X1.size)
Y=map(lambda x1,x2: f(x1,x2),X1,X2)

Y=np.asarray(list(Y))
print(Y)
print(Y.shape)
print(X1.shape)

fig=plt.figure()
# ax=Axes3D(fig)
ax=fig.add_axes(Axes3D(fig))  # 生成一个3d作图对象

ax.plot_surface(X1,X2,Y,cmap=plt.cm.jet)  # 用3d对象做曲面,rgb
# ax.plot_surface(X1,X2,Y,cmap=plt.cm.gray)  # 用3d对象做曲面,灰度图
plt.show()

