#include <iostream>

using namespace std;

void sayHi(string name, int age){
    cout << "Hello " << name << " you are "<< age << endl;
}

int main() {

    cout << "Top\n";
    sayHi("FER", 31); 
    sayHi("Pete", 23); 
    sayHi("Luisa", 20); 
    cout << "Bottom\n";
    return 0;
}