import serial
import time
import pyautogui
from collections import deque
import cv2
import numpy as np

def conv_img_to_ser_deque(img):
    threshold_val = 255
    m, n = img.shape
    tmp_deque = deque()
    col = 0
    for row in img:
        row_deque = deque(row)
        cnt = 0
        flag = -1
        if col % 2 == 0:
            while row_deque:
                tmp = row_deque.popleft()
                if tmp == 0 and flag == 0:
                    cnt += 1
                elif tmp == 0:
                    if flag != -1:
                        tmp_deque.append(str(cnt))
                        tmp_deque.append('`')
                    tmp_deque.append('P')
                    tmp_deque.append('`')
                    tmp_deque.append('r')
                    cnt = 1
                    flag = 0
                elif tmp == threshold_val and flag == 1:
                    cnt += 1
                elif tmp == threshold_val:
                    if flag != -1:
                        tmp_deque.append(str(cnt))
                        tmp_deque.append('`')
                    tmp_deque.append('p')
                    tmp_deque.append('`')
                    tmp_deque.append('r')
                    cnt = 1
                    flag = 1
        else:
            while row_deque:
                tmp = row_deque.pop()
                if tmp == 0 and flag == 0:
                    cnt += 1
                elif tmp == 0:
                    if flag != -1:
                        tmp_deque.append(str(cnt))
                        tmp_deque.append('`')
                    tmp_deque.append('P')
                    tmp_deque.append('`')
                    tmp_deque.append('l')
                    cnt = 1
                    flag = 0
                elif tmp == threshold_val and flag == 1:
                    cnt += 1
                elif tmp == threshold_val:
                    if flag != -1:
                        tmp_deque.append(str(cnt))
                        tmp_deque.append('`')
                    tmp_deque.append('p')
                    tmp_deque.append('`')
                    tmp_deque.append('l')
                    cnt = 1
                    flag = 1
        if cnt == n:
            tmp_deque.pop()
            tmp_deque.pop()
            tmp_deque.append('`')
        else:
            tmp_deque.append(str(cnt))
            tmp_deque.append('`')
            col += 1
        tmp_deque.append('d')
        tmp_deque.append('1')
        tmp_deque.append('`')
    
    ans_deque = deque()
    while tmp_deque:
        tmp = tmp_deque.popleft()
        try:
            if tmp == 'd' and tmp_deque[4] == 'd':
                down_num = int(tmp_deque[0])
                tmp_deque.popleft()
                tmp_deque.popleft()
                tmp_deque.popleft()
                tmp_deque.popleft()
                tmp_deque[1] = str(down_num + 1)
            else:
                ans_deque.append(tmp)
        except:
            ans_deque.append(tmp)
    return ans_deque

def conv_ser_deque_to_img(ser_deque, img_shape):
    threshold_val = 255
    ans_img = np.zeros(img_shape)
    x, y = 0, 0
    solenoid_state = 0
    while ser_deque:
        tmp = ser_deque.popleft()
        if tmp == 'd':
            y += int(ser_deque.popleft())
        elif tmp == 'p':
            solenoid_state = 1
            ser_deque.popleft()
        elif tmp == 'P':
            solenoid_state = 0
            ser_deque.popleft()
        elif tmp == 'r':
            r_mov_dis = int(ser_deque.popleft())
            _ = ser_deque.popleft()
            while r_mov_dis != 0:
                if solenoid_state == 1:
                    ans_img[y][x] = threshold_val
                x += 1
                r_mov_dis -= 1
        elif tmp == 'l':
            l_mov_dis = int(ser_deque.popleft())
            _ = ser_deque.popleft()
            while l_mov_dis != 0:
                x -= 1
                if solenoid_state == 1:
                    ans_img[y][x] = threshold_val
                l_mov_dis -= 1
    return ans_img

img_file_name = 'input7'

img = cv2.imread('capstone/' + img_file_name + '.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0, 0), fx=1, fy=1)
_, img = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
cv2.imwrite('capstone/' + img_file_name + '_img_proc_v3.png', img)
serial_deque = conv_img_to_ser_deque(img)

print(serial_deque)

def interact_ser(_str, _ard):
    _ard.write(_str.encode())
    tmp = _ard.readline()
    print(tmp.decode())
    
if __name__ == "__main__":
    port = 'COM10'  # 변동가능
    ard = serial.Serial(port, 9600)
    time.sleep(2)

    for i in serial_deque:
        if list(pyautogui.position()) != [0, 0]:
            interact_ser(i, ard)

    ard.close()
