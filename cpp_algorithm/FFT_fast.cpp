#include<iostream>
#include<complex>
#include<vector>
#include<cmath>
#include<algorithm>

using namespace std;

const double PI = 3.1415926535897932384626433832795028841971693993751058209749445923078;
typedef complex<double> cpx;

void FFT(vector<cpx> &x, bool inv)
{
    int l = x.size();
    int e = 0;
    while(l > 1 << e) e += 1;
    for(int i = 0; i < l; ++i)
    {
        int tmp = 0;
        for(int j = 0; j < e; ++j)
        {
            if((i & 1 << j) > 0) tmp += 1 << (e - j - 1);
        }
        if(tmp > i) swap(x[tmp], x[i]);
    }

    for(int i = 1; i <= e; ++i)
    {
        int n = 1 << i;
        cpx w;
        if(inv) w = cpx(cos(2 * PI / n), sin(2 * PI / n));
        else w = cpx(cos(2 * PI / n), -sin(2 * PI / n));
        for(int j = 0; j < l; j += n)
        {
            cpx wp = cpx(1, 0);
            for(int k = j; k < j + n / 2; ++k)
            {
                cpx tmp = x[k];
                x[k] = tmp + wp * x[k + n / 2];
                x[k + n / 2] = tmp - wp * x[k + n / 2];
                wp *= w;
            }
        }
    }
    if(inv)
    {
        for(int i = 0; i < l; ++i) x[i] /= l;
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

    FFT(_arr1, false);
    FFT(_arr2, false);

    for(int i = 0; i < _N; ++i)
        _ans[i] = _arr1[i] * _arr2[i];
    
    FFT(_ans, true);
    for(int i = 0; i < _N; ++i)
    {
        _ans[i] /= cpx(_N, 0);
        _ans[i] = cpx(round(_ans[i].real()), round(_ans[i].imag()));
    }
    return _ans;
}

int main()
{
    int N = 32;
    vector<cpx>a(N);
    for(int i = 0; i < N; ++i) a[i] = cpx(i, 0);
    FFT(a, false);
    cout << 1;
}