#include <iostream>
#include "string.h"
using namespace std;

struct client
{
    char Name[50];
    char Id[10];
    float Credit;
    char Address[100];
};

int main() {

    struct client client1 = {0};
    strcpy(client1.Name , "Camilo Valencia");
    strcpy(client1.Id , "0000000001");
    client1.Credit = 1000000;
    strcpy(client1.Address , "Calle 1, Carrera 1 Ciudad bolivar");

    printf("The client name is: %s \n", client1.Name);
    printf("The client Id is: %s \n", client1.Id);
    printf("The client Credit is: %f \n", client1.Credit);
    printf("The client Address is: %s \n", client1.Address);

    return 0;
}