#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {

    int frequency = 0;
    string input;
    ifstream infile(argv[1]);
    int val;

    while(infile >> input) {
        val = stoi(input);
        frequency += val;
    }

    cout << "Ending frequency: " << frequency << "\n";

    return 0;
}