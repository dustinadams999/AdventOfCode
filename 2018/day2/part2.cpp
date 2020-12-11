#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {

    string input, code;
    ifstream infile(argv[1]);
    int differences = 0, i, j, k;
    vector<string> codes;


    while (infile >> input) {
        codes.push_back(input);
    }

    for (i = 0; i < codes.size(); i++) {
        code = codes[i];
        for (j = i+1; j < codes.size(); j++) {
            differences = 0;
            for (k = 0; k < code.size(); k++) {
                if (codes[i][k] != codes[j][k]) {
                    differences++;
                }
            }
            cout << "differences for i=" << i << ", j=" << j << ": " << differences << "\n";
            if (differences == 1) {
                cout << "WE FOUND OUR MATCH: \n" << codes[i] << "\n" << codes[j] << "\n";
                return 0;
            }
        }
    }

    return 0;
}









