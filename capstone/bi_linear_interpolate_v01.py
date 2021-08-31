import numpy as np
import cv2


def bilinear_interpolate(_np_gray_image, _p1, _p2, _p3, _p4): # p1: ll, p2: lh, p3: hl, p4: hh
    x_max = max(_p1[0], _p2[0], _p3[0], _p4[0])
    y_max = max(_p1[1], _p2[1], _p3[1], _p4[1])
    n = 2
    ans = np.zeros((x_max, y_max , 2))
    for i in range(x_max * n):
        for j in range(y_max * n):
            u = i / (x_max * n)
            v = j / (y_max * n)
            x = round((1 - u) * ((1 - v) * _p1[0] + v * _p2[0]) + u * ((1 - v) * _p3[0] + v * _p4[0]))
            y = round((1 - u) * ((1 - v) * _p1[1] + v * _p2[1]) + u * ((1 - v) * _p3[1] + v * _p4[1]))
            try:
                ans[x][y][0] = (ans[x][y][0] * ans[x][y][1] + _np_gray_image[round(_np_gray_image.shape[0] * u)][round(_np_gray_image.shape[1] * v)]) / (ans[x][y][1] + 1)
                ans[x][y][1] += 1
            except:
                pass
    return ans[:, :, 0]

if __name__ == '__main__':
    image = cv2.imread(("python/test3.png"), cv2.IMREAD_GRAYSCALE)
    image = 255 - image
    img_y, img_x = image.shape
    print(img_x, img_y)

    a = 2000
    h = 130
    y = 39

    image = cv2.resize(image, dsize=(0, 0), fx=y / img_y, fy=y / img_y, interpolation=cv2.INTER_LINEAR)
    img_y, img_x = image.shape
    x = img_x
    Y = int(a * y / (h - y))
    X = int(x * (Y + a) / a)
    print(X, Y)
    print(img_x, img_y)

    p1 = (0, 0)
    p2 = (0,    X)
    p3 = (Y, X // 2 - img_x // 2)
    p4 = (Y, X // 2 + img_x // 2)
    name = bilinear_interpolate(image, p1, p2, p3, p4)
    _, name = cv2.threshold(name, 100, 255, cv2.THRESH_BINARY)
    name = cv2.GaussianBlur(name, (3,3), 0)
    _, name = cv2.threshold(name, 1, 255, cv2.THRESH_BINARY)
    cv2.imwrite("python/output3.png", name)