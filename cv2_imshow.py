import cv2
import numpy
import matplotlib.pyplot as plt

x = numpy.random.randn(512, 512)
cv2.imshow('test', x)
cv2.waitKey(0)

plt.figure("Image") # 图像窗口名称
plt.imshow(x, cmap='gray')
plt.axis('off')
plt.show()
