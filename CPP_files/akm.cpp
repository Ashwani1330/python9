#include <iostream>
using namespace std;

template<class T>

T sum (T x, T y)
{
    return (x + y);
}

int main()
{
    int result = sum<int> (2, 5);
    cout << "Result when integer values are passed is: " << result << endl;
    double result2 = sum<double> (2.5, 5.5);
    cout << "Result when double values are passsed is: " << result2 << endl;
    return 0;
}