#include <iostream>
using namespace std;

int main() {
    string phrase = "Academy Cpp";
    string phrasesub;
    phrasesub = phrase.substr(8, 1);

    cout << phrasesub;
    return 0;
}

// length find substr