#include <iostream>
#include "main.hh"
#include "hello/hello.hh"

using namespace std;

int main()
{
    cout << "Hello there!\n";
    cout << "1 + 1 = " << add(1, 1) << endl;

    Hello *hi = new Hello();
    hi->greet();
    hi->greet();
    delete hi;

    return 0;
}
