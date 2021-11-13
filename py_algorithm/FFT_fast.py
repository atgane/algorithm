import math

def FFT(x, inv = False):
    l = len(x)
    e = 0
    while l > 1 << e: e += 1

    for i in range(l):
        tmp = 0
        for j in range(e):
            if i & 1 << j > 0:
                tmp += 1 << (e - j - 1)
        if tmp > i:
            x[i], x[tmp] = x[tmp], x[i]
            
    for i in range(1, e + 1):
        n = 1 << i
        w = complex(math.cos(2 * math.pi / n), math.sin(2 * math.pi / n) * (1 if inv else -1))
        for j in range(0, l, n):
            wp = 1 + 0j
            for  k in range(j, j + n // 2):
                x[k], x[k + n // 2] = x[k] + wp * x[k + n // 2], x[k] - wp * x[k + n // 2]
                wp *= w
    
    if inv:
        for i in range(l): x[i] /= l

def conv(_arr1, _arr2):
    _N = 1
    while((_N < len(_arr1) + 1) and (_N < len(_arr2) + 1)):
        _N *= 2
    _N *= 2
    _arr1 += [0 for _ in range(_N - len(_arr1))]
    _arr2 += [0 for _ in range(_N - len(_arr2))]
    _ans = [0 for _ in range(_N)]
    
    FFT(_arr1)
    FFT(_arr2)

    for i in range(_N):
        _ans[i] = _arr1[i] * _arr2[i]
    
    FFT(_ans, True)
    for i in range(_N):
        _ans[i] = round(_ans[i].real)
    return _ans