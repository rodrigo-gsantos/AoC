#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int id = 1, sum = 0, max = 0, idMax = 0;
    string value;
    vector<int> calories;
    while(getline(cin, value)){
        if(value == ""){
            if(sum > max){
                idMax = id;
                max = sum;
            }
            calories.push_back(sum);
            id++;
            sum = 0;
        }
        else{
            sum += stoi(value, nullptr, 10);
        }
    }
    sort(calories.begin(), calories.end());
    for (auto x : calories)
        cout << x << "\n";
    long int last3 = calories[calories.size()-1] + calories[calories.size()-2] + calories[calories.size()-3];
    printf("Elf number: %d \nCalories: %d\nLast3: %d\n", idMax, max, last3);
    return 0;
}