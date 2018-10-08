#include <iostream>

class Dog{
    std::string name;
    int weight;

    public:
        Dog();

        void setName(std::string & dogName);
    
        void setWeight(int dogWeight);
        
        virtual void print() const;

        void bark() const {std::cout<< name << " barks\n";}

        virtual ~Dog();
};

