import numpy
import cv2


n = numpy.arange(27)
n = n.reshape(3, 3, 3)

im_g = cv2.imread("data/img1.jpg", 1)


print(im_g)

def test(t: [int]) -> [int]:
    return t

print(test([1,2,3]))