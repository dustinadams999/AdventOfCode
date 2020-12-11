#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {

    string input;
    ifstream infile(argv[1]);

    int two_times = 0;
    int three_times = 0;
    int count, i, j, k;
    bool two = false, three = false, already = false;

    while (infile >> input) {
        string checked_chars = "";
        two = false;
        three = false;
        for (i = 0; i < input.size()-1; i++) {
            already = false;
            // determine if the letter has already been checked
            for (j = 0; j < checked_chars.size(); j++) {
                if (input[i] == checked_chars[j]) {
                    already = true;
                    break;
                }
            }
            if (already) {
                continue;
            }
            else {
                // count how many times the character appears
                count = 0;
                for (k = 0; k < input.size(); k++) {
                    if (input[i] == input[k]) {
                        count++;
                    }
                }
                if (count == 2) {
                    // only count each token with 2 char occurances once
                    if (!two) {
                        two_times++;
                        two = true;
                    }
                }
                else if (count == 3) {
                    if (!three) {
                        three_times++;
                        three = true;
                    }
                }
            }
            checked_chars += input[i];
        }
    }
    cout << "RESULT: " << two_times << ", " << three_times << ", " << two_times * three_times << "\n";

    return 0;
}