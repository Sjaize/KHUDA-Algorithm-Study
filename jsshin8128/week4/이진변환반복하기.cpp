#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;

    int transformCount = 0;
    int zeroCount = 0;

    while (s != "1") {
        int currentZeroCount = 0;
        string noZeros = "";

        for (char c : s) {
            if (c == '0') {
                currentZeroCount++;
            }
            else {
                noZeros += c;
            }
        }

        zeroCount += currentZeroCount;
        int length = noZeros.length();

        string binary = "";
        while (length > 0) {
            binary = to_string(length % 2) + binary;
            length /= 2;
        }

        s = binary;
        transformCount++;
    }

    answer.push_back(transformCount);
    answer.push_back(zeroCount);
    return answer;
}