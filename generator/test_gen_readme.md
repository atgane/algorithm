# 테스트 케이스 제너레이터 만들기

1. gen.py에서 랜덤 케이스 생성하여 1.txt 파일로 저장
2. gen_act.py에서 쉘 스크립트를 실행하여 오답코드와 정답코드 실행.
3. 오답코드와 정답코드는 각각 출력을 out1.txt, out2.txt에 저장
4. gen_act.py에서 out1.txt, out2.txt의 값 읽고 비교


# 파이썬의 경우

## 입력의 경우

1. 파이썬 파일에 직접 입력

```python
sys.stdin = open('1.txt', 'r')
```

2. 쉘 스크립트 입력

```shell
python test.py < 1.txt
```

## 출력의 경우

1. 파이썬 파일에 직접 입력

```python
sys.stdout = open('output.txt','w')
```
2. 쉘 스크립트 입력

```shell
python test.py > 1.txt
```

## 정리

다음을 코드 윗 줄에 입력

오답코드
```python
import sys
sys.stdin = open('1.txt', 'r')
sys.stdout = open('out1.txt', 'w')
#ssr = sys.stdin.readline
```

정답코드
```python
import sys
sys.stdin = open('1.txt', 'r')
sys.stdout = open('out2.txt', 'w')
#ssr = sys.stdin.readline
```

# C++의 경우

```C++
#include <fstream>
 
using namespace std;
 
int main()
{
    cin.tie(0);
 
    // 읽기(바로 콘솔창으로 바로 입력하게 함)
    freopen("1.txt", "r", stdin);
 


    
    // 출력값들을 메모장에 쓸 때(파일명으로 생성)
    ofstream fout;
    fout.open("out1.txt");
    fout << "test\n";
    fout.close();
 
    return 0;
}
```

## 정리
```C++
#include <fstream>
using namespace std;

int main()
{
    freopen("1.txt", "r", stdin);
    ofstream fout;
    fout.open("out1.txt");
    //모든 cout을 fout으로 변경



    fout.close();
}
```