#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int points = 0;
    int part2Points = 0;
    string value;
    while(getline(cin, value)) {
        if(value == "A X"){ // A B C Pedra Papel Tesoura X Y Z
            points += 4;
            part2Points += 3;
        }
        else if (value == "A Y"){
            points += 8;
            part2Points += 4;
        }
        else if (value == "A Z"){
            points += 3;
            part2Points += 8;
        }
        else if (value == "B X"){
            points += 1;
            part2Points += 1;
        }
        else if (value == "B Y"){
            points += 5;
            part2Points += 5;
        }
        else if (value == "B Z"){
            points += 9;
            part2Points += 9;
        }
        else if (value == "C X"){
            points += 7;
            part2Points += 2;
        }
        else if (value == "C Y"){
            points += 2;
            part2Points += 6;
        }
        else if (value == "C Z"){
            points += 6;
            part2Points += 7;
        }
        //cout << points << "\n";
        cout << part2Points << "\n";
    }
}