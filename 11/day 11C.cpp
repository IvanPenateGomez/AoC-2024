#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int part1() {
    vector<int> arr = {0, 5601550, 3914, 852, 50706, 68, 6, 645371};

    for (int iteration = 0; iteration < 75; ++iteration) {
        vector<int> tempArr;

        for (int s : arr) {
            if (s == 0) {
                tempArr.push_back(1);
            } else {
                int v = static_cast<int>(log10(s)) + 1;
                if (v % 2 == 0) {
                    int divisor = static_cast<int>(pow(10, v / 2));
                    tempArr.push_back(s / divisor);
                    tempArr.push_back(s % divisor);
                } else {
                    tempArr.push_back(s * 2024);
                }
            }
        }

        arr = tempArr;
    }

    return arr.size();
}

int main() {
    cout << part1();
    return 0;
}