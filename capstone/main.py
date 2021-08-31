from bi_linear_interpolate_v01 import *

if __name__ == '__main__':
    image = cv2.imread(("python/test3.png"), cv2.IMREAD_GRAYSCALE)
    image = 255 - image
    img_y, img_x = image.shape
    print(img_x, img_y)

    a = 2000
    h = 130
    y = 39
    bar_y = 19

    image = cv2.resize(image, dsize=(0, 0), fx=(y - bar_y) / img_y, fy=(y - bar_y) / img_y, interpolation=cv2.INTER_LINEAR)
    img_y, img_x = image.shape
    x = img_x
    Y = int(a * y / (h - y))
    bar_Y = int(a * bar_y / (h - bar_y))
    X = int(x * (Y + a) / a)
    bar_X = int(x * (bar_Y + a) / a)
    out_Y = Y - bar_Y
    print(X, bar_X , out_Y)
    print(img_x, img_y)

    p1 = (0, 0)
    p2 = (0,    X)
    p3 = (out_Y, X // 2 - bar_X // 2)
    p4 = (out_Y, X // 2 + bar_X // 2)
    name = bilinear_interpolate(image, p1, p2, p3, p4)
    _, name = cv2.threshold(name, 100, 255, cv2.THRESH_BINARY)
    name = cv2.GaussianBlur(name, (3,3), 0)
    _, name = cv2.threshold(name, 1, 255, cv2.THRESH_BINARY)
    cv2.imwrite("python/output3.png", name)