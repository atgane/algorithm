def computeLPS(_pat, _lps):
    _length = 0
    _N = len(_pat)
    i = 1
    while i < _N:
        if _pat[_length] == _pat[i]:
            _length += 1
            _lps[i] += _length
            i += 1
        else:
            if _length != 0:
                _length = _lps[_length - 1]
            else:
                i += 1

def KMPSearch(_pat, _txt):
    i = 0
    j = 0
    _N = len(_txt)
    _M = len(_pat)
    _lps = [0 for _ in range(_N)]
    computeLPS(_pat, _lps)
    while i < _N:
        if _pat[j] == _txt[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = _lps[j - 1]
            else:
                i += 1
        if j == _M:
            print("same index:", i - j)
            j = _lps[j - 1]