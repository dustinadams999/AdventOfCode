#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {

    int frequency = 0;
    vector<int> frequencies;
    frequencies.push_back(frequency);
    int j = 0;
    while(true) {
        cout << "NEW PASS: " << j << ", length of freqs: " << frequencies.size() << "\n";
        string input;
        ifstream infile(argv[1]);
        int val;

        while(infile >> input) {
            val = stoi(input);
            frequency += val;
            // search through frequencies
            for(int i = 0; i < frequencies.size(); i++) {
                if (frequencies[i] ==  frequency) {
                    cout << "DUPLICATE FOUND at frequency: " << frequency << "\n" ;
                    return 0;
                }
            }
            frequencies.push_back(frequency);
        }
        j++;
    }
    //return 0;
}