/*************************************************************************
	> File Name: demo.cpp
	> Author: 
	> Mail: 
	> Created Time: 日  9/16 00:23:32 2018
 ************************************************************************/

#include<iostream>
#include <map>
using namespace std;

int main(int argc, const char * argv[1]){
    //访问字符串的几种形式
    /*
    cout << a[0] << endl;
    cout << a.size() << endl;
    cout << sizeof(a) << endl;
    */
    /*
    short a = 4294967296;
    cout << sizeof(char) << endl;
    cout << sizeof(int) << endl;
    cout << sizeof(bool) << endl;
    cout << sizeof(short) << endl;
    cout << sizeof(float) << ' ' << sizeof(long) << " " << sizeof(long long) << endl;
    cout << a << endl;
    */

    map<int, int> res = map<int, int>();
    res[7] = 1;
    res[9] = 2;
    cout << res.size() << endl;
    cout << res[0] << endl;
    cout << res.count(8) << endl;
    return 0;
}
