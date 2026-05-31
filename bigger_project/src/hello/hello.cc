#include "hello.hh"
#include <iostream>
using namespace std;

Hello::Hello()
{
    cout << "Creting Hello object\n";
}

void Hello::greet()
{
    this->count++;
    cout << "Hello there! You have been greeted " << this->count << " time(s)!\n";
}
