#include <iostream>
#include <sstream>
#include <string>
#include "Utils.hpp"

using namespace std;

void showMenu(){
    cout << "====Menu====\n";
    cout << "0. Exit program\n";
    cout << "1. Shutdown (user input)\n";
    cout << "2. Shutdown (predefined intervals)\n";
}

void showUserShutdownMenu(){
    cout << "====Shutdown (user input)====\n";
    cout << "Introduce duration (seconds): ";

    int seconds;
    cin >> seconds;

    executeShutdown(seconds);
}

void showPredefinedShutdownMenu(){
    int choice = 255;

    do{
        cout << "====Shutdown (predefined intervals)====\n";
        cout << "0. Go back\n";
        cout << "1. 1h (3600s)\n";
        cout << "2. 2h (7200s)\n";
        cout << "3. 3h (10800s)\n";
        cout << "Pick: ";

        cin >> choice;

        switch(choice){
            case 0:
                break;
            case 1:
                system("timeout -t 3600 && shutdown -s -f -t 0");
                break;
            case 2:
                system("timeout -t 7200 && shutdown -s -f -t 0");
                break;
            case 3:
                system("timeout -t 10800 && shutdown -s -f -t 0");
                break;
            default:
                cout << "Invalid pickkkk\n";
        }
    } while(choice != 0);
}

void executeShutdown(int time){
    stringstream shutdownCommand;
    shutdownCommand << "timeout -t " << time << " && shutdown -s -f -t 0";
    system(shutdownCommand.str().c_str());
    cout << "Program will now exit";
}