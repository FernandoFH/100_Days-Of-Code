#include <iostream>
#include <cmath>

using namespace std;

int main(){

    string color, pluralNoum, celebrity;

    cout << "Enter a color:";
    getline(cin, color);

    cout << "Enter a plural noum:";
    getline(cin, pluralNoum);

    cout << "Enter a celebrity:";
    getline(cin, celebrity);

    cout << "Roses are " << color << endl;
    cout << pluralNoum <<" are blue" << endl;
    cout << "I love " << celebrity << endl;

    return 0;
}