 #include <iostream> 
 using namespace std;

class Client {
    public:
        string Name;
        string Id;
        double Credit;
        string Address;

        Client(string aName, string aId, double aCredit, string aAddress){
            Name= aName;
            Id = aId;
            Credit = aCredit; 
            Address = aAddress;
        }
    
};

int main(){

    Client client1("Fernando Hernandez","0000000002",2000,"Av. 1 CABA" );

    cout << "The client name is: " << client1.Name << endl;
    cout << "The client Id is: " <<  client1.Id << endl;
    cout << "The client Credit is: " <<  client1.Credit << endl;
    cout << "The client Address is: " <<  client1.Address << endl;

    return 0;
}