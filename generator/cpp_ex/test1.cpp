#include<fstream>
#include<iostream>

using namespace std;

int main()
{
    cin.tie(0);
    
    // 읽기(바로 콘솔창으로 바로 입력하게 함)
    freopen("1.txt", "r", stdin);
    ofstream fout;
    
    int a; cin >> a;

    // 출력값들을 메모장에 쓸 때(파일명으로 생성)
    
    fout.open("out1.txt");
    fout << 3 << "\n";
    fout.close();

    return 0;
}
