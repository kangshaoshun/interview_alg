/*************************************************************************
	> File Name: high.cpp
	> Author: 
	> Mail: 
	> Created Time: 六  8/25 19:29:23 2018
 ************************************************************************/

#include<iostream>
#include "demo.hpp"
using namespace std;


//类与面向对象
Dog::Dog(){
    std::cout << "liuxiaochuang has been created" << std::endl;
}

void Dog::setName(std::string& dogName){
    name = dogName;
}

void Dog::setWeight(int dogWeight){
    weight = dogWeight;
}

void Dog::print()const{
    std::cout << name << "  " << weight << std::endl;
}

Dog::~Dog(){
    std::cout << "liuxiaochuang has dead" << std::endl;
}

int main(){
    Dog dog;
    string name = "liuxiaochuang";
    dog.setName(name);
    dog.setWeight(190);
    dog.print();
    return 0;
}
