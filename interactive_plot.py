import matplotlib.pyplot as plt
import numpy as np
from skimage import data, exposure, transform
from mpl_toolkits.mplot3d import axes3d

shape = np.floor(np.asarray(data.rocket().shape[0:2])/10).astype(dtype=np.int)
shape = np.hstack((shape, 3))
im =  transform.resize(data.rocket(),shape)
plt.figure(figsize=(10, 5))
plt.imshow(im)
plt.figure()
r = im[:, :, 0]
g = im[:, :, 1]
b = im[:, :, 2]
ax = plt.axes(projection='3d')
plt.scatter(r.ravel(), g.ravel(), b.ravel(), cmap='viridis', linewidth=0.5)
plt.show()