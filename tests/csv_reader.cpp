#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream file;
    file.open("../include/watched.csv");
    string line;
    getline(file, line);
    
    while (getline(file, line, ',')) {
        cout << line << endl;
    }

    file.close();
    return 0;
}
