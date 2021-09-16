import cv2

test0 = cv2.imread('capstone/input2.png', cv2.IMREAD_GRAYSCALE)
print(test0.shape)
print(test0)


test1 = cv2.imread('capstone/input2_img_proc_v2.png', cv2.IMREAD_GRAYSCALE)
print(test1.shape)
print(test1)

test2 = cv2.imread('capstone/input2_img_conv_v2.png', cv2.IMREAD_GRAYSCALE)
print(test2.shape)
print(test2)
