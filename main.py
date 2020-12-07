from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

image = Image.open('ASHE-PF.jpg')
# image.show()
plt_image = plt.imread('ASHE-PF.jpg')
plt.imshow(plt_image)
plt.show()

print(image.format)
print(image.mode)
print(image.size)
print(image.palette)

def resize(image, length, height):
    new_image = image.resize((length,height))
    new_image.save('new_image.jpg')
    print(new_image.size)
    new_image.show()


def get_info():
    print('enter l n h:\n')
    length, height = [int(x) for x in input().split()]
    resize(image, length, height)


# get_info()






# new_image.show()