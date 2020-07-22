#include <iostream>
using namespace std;

int main() {

    string characterName = "Fernando";
    int characterAge;
    characterAge = 31;

    cout << "There onces was a man named " << characterName << endl;
    cout << "He was " << characterAge << " years old" << endl;

    characterName ="Mike";
    cout << "There onces was a man named " << characterName << endl;
    cout << "He was " << characterAge << " years old" << endl;

    return 0;
}

// g++ -o variables.exe variables.cpp