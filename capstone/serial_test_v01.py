import serial


def interact_ser(_str, _ard):
    _ard.write(_str.encode())
    tmp = _ard.readline()
    print(tmp.decode())


if __name__ == "__main__":
    port = 'COM6'  # 변동가능
    ard = serial.Serial(port, 9600)

    while True:
        send_str = input()
        if send_str == '-':
            break
        else:
            interact_ser(send_str, ard)

    ard.close()
