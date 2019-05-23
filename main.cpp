#include <iostream>
#include "Utils.hpp"

using namespace std;

int main() {
    int choice = 255;
    do{
        showMenu();
        cout << "User's pick: ";
        cin >> choice;
            switch(choice){
                case 0:
                    break;
                case 1:
                    showUserShutdownMenu();
                    break;
                case 2:
                    showPredefinedShutdownMenu();
                default:
                    cout << "Invalid pick\n";
            }
        } while(choice != 0);

    cout << "Exiting...";
    return 0;
}
