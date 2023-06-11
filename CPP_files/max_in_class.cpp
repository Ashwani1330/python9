#include <iostream>
using namespace std;

template <class T>
T maxNum(T x, T y)
{
    return (x > y ? x : y);
}

int main()
{
    int a = 5, b = 2;
    float i = 4.5, j = 1.3;
    cout << maxNum<int> (a, b) << endl;
    cout << maxNum<float> (i, j) << endl;
    return 0;
}