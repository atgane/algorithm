import math

def FFT(_arr, _w):
    _N = len(_arr)
    if _N == 1:
        _ = 1
    else:
        _even = []
        _odd = []
        for i in range(_N):
            _even.append(_arr[i]) if i % 2 == 0 else _odd.append(_arr[i])

        FFT(_even, _w * _w)
        FFT(_odd, _w * _w)

        _wp = 1 + 0j
        for i in range(0, _N // 2):
            _arr[i] = _even[i] + _wp * _odd[i];
            _arr[i + _N // 2] = _even[i] - _wp * _odd[i];
            _wp *= _w

def conv(_arr1, _arr2):
    _N = 1
    while((_N < len(_arr1) + 1) and (_N < len(_arr2) + 1)):
        _N *= 2
    _N *= 2
    _arr1 += [0 for _ in range(_N - len(_arr1))]
    _arr2 += [0 for _ in range(_N - len(_arr2))]
    _ans = [0 for _ in range(_N)]
    
    _w = complex(math.cos(2 * math.pi / _N), math.sin(2 * math.pi / _N))
    FFT(_arr1, _w)
    FFT(_arr2, _w)

    for i in range(_N):
        _ans[i] = _arr1[i] * _arr2[i]
    
    FFT(_ans, 1 / _w)
    for i in range(_N):
        _ans[i] /= _N
        _ans[i] = complex(round(_ans[i].real), round(_ans[i].imag))
    return _ans