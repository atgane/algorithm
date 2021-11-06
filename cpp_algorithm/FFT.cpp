#include<iostream>
#include<complex>
#include<vector>
#include<cmath>

using namespace std;

const double PI = 3.1415926535897932384626433832795028841971693993751058209749445923078;
typedef complex<double> cpx;

void FFT(vector<cpx> &_arr, cpx _w)
{
    int _N = _arr.size();
    if(_N == 1) return;

    vector<cpx> _even(_N / 2), _odd(_N / 2);
    for(int i = 0; i < _N; ++i)
    {
        if(i % 2 == 0)
            _even[i / 2] = _arr[i];
        else
            _odd[i / 2] = _arr[i];
    }

    FFT(_even, _w * _w);
    FFT(_odd, _w * _w);
    
    cpx _wp(1, 0);
    for(int i = 0; i < _N / 2; ++i)
    {
        _arr[i] = _even[i] + _wp * _odd[i];
        _arr[i + _N / 2] = _even[i] - _wp * _odd[i];
        _wp *= _w;
    }
}

vector<cpx> conv(vector<cpx> _arr1, vector<cpx> _arr2)
{
    int _N = 1;
    while(_N < _arr1.size() + 1 || _N < _arr2.size() + 1)
        _N <<= 1;
    _N <<= 1;
    _arr1.resize(_N);
    _arr2.resize(_N);
    vector<cpx> _ans(_N);

    double t = 2 * PI / _N;
    cpx _w(cos(2 * PI / _N), sin(2 * PI / _N));

    FFT(_arr1, _w);
    FFT(_arr2, _w);

    for(int i = 0; i < _N; ++i)
        _ans[i] = _arr1[i] * _arr2[i];
    
    FFT(_ans, cpx(1, 0) / _w);
    for(int i = 0; i < _N; ++i)
    {
        _ans[i] /= cpx(_N, 0);
        _ans[i] = cpx(round(_ans[i].real()), round(_ans[i].imag()));
    }
    return _ans;
}