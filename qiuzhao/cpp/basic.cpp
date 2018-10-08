/*************************************************************************
	> File Name: demo.cpp
	> Author: 
	> Mail: 
	> Created Time: 六  8/25 16:03:09 2018
 ************************************************************************/

#include<iostream>
using namespace std;
void dosomething(int a=1, int b=2){
    cout << a * 2 + b << endl;
}


namespace First{
    namespace Nested{
        void foo(){
            cout << "this is first nested foo"<<endl;
        }
    }
}

namespace Second{
    void foo(){
        cout << "this is second::foo" << endl;
    }
}

void foo(){
    cout<<"this is a global foo"<<endl;
}

int main(){
    /*
    cout<< "are you ok" << endl;
    cout << sizeof(char) << endl;
    cout << sizeof(int) << endl;
    
    //空指针
    int* a = nullptr;
    if(!a){cout<<"yes"<<endl;}
    printf("are you ok");
    
    //默认参数
    dosomething(3, 4);
    dosomething();
    dosomething(2);

    //命名空间
    foo();
    First::Nested::foo();
    Second::foo();
    
    //iostream
    int a, b;
    cout << "please input your number" << endl;
    cin >> a;
    cin >> b;
    cout << 2 * a + b << endl;
    cerr << "wrong answer";
    
    //string
    string myString = " he";
    string myOtherString = " world";
    cout << myString + myOtherString << endl;
    cout << myString + " you" << endl;
    cout << sizeof(myString) << endl;
    myString.append("kangshaoshun");
    cout << sizeof(myString) << endl;
    cout << myString << endl;
    cout << myString.size() << endl;
    myString[2] = 'r';
    cout << myString << endl;
    auto begin = myString.begin();
    auto end = myString.end();
    while (begin != end){
        cout << *begin << ' ';
        begin ++ ;
    }

    //引用
    string foo = "I am foo";
    string bar = "I am bar";
    string& ref = foo;
    cout << ref << endl;
    cout << &ref << endl;
    ref = bar;
    cout << &ref << endl;
    cout << ref << endl;
    foo = "I am foo";
    const string& barref = foo;
    cout << barref << endl;
    */

    //enum 枚举
    enum Name{
        kang,
        shao,
        shun
        };
    cout << Name::kang << endl;
    


}

