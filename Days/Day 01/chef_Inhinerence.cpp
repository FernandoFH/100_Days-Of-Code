#include <iostream>
using namespace std;

class Chef {
    public:
        void makeChicken(){
            cout << "The chef makes chicken" << endl;
        }
        void makeSalad(){
            cout << "The chef makes salad" << endl;
        }
        void makeSpecialDish(){
            cout << "The chef makes BBQ Ribs" << endl;
        }
};

class ItalianChef : public Chef{
    public:
        void makePasta(){
            cout << "The chef makes pasta" << endl;
        }
        void makeSpecialDish(){
            cout << "The chef makes chicken parm" << endl;
        }
};


int main(){

    Chef chef;
    chef.makeSpecialDish();

    ItalianChef italianChef;
    italianChef.makeSpecialDish();

    return 0;
}