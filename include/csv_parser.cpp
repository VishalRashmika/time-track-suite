#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

#include "csv_parser.h"

using namespace std;

vector<vector<string>> CSV_parser::read_csv(std::string filepath)
{

    // std::string location{"/home/akira/Downloads/letterboxd-akiraarashikage-2024-07-20-04-10-utc/wathched.csv"};

    ifstream infile(filepath);
    vector<vector<string>> rows;

    // std::cout << "Location : " << location << std::endl;
    
    // Read CSV into rows
    string line;
    int counter;
    while (getline(infile, line))
    {
        vector<string> row;
        counter = 0;
        string field;
        stringstream ss(line);

        while (getline(ss, field, ','))
        {
            if (counter == 1 || counter == 3)
            {
                row.push_back(field);
            }
            counter += 1;
        }
        rows.push_back(row);
    }

    // std::cout << rows.size() << std::endl;
    // std::cout << rows[1][0] << std::endl/;

    return rows;
}

// int main()
// {
//     std::vector<std::vector<std::string>> data;
//     std::string filepath{"./watched.csv"};
//     data = read_csv(filepath);
//     for (int i = 0; i < data.size(); i++){
//         for (int j = 0; j < 2; j++){
//             std::cout << data[i][j] << std::endl;
//         }
//     }
//     return 0;
// }

/*
//   // Create a new record
//   vector<string> newRecord {"Sam", "35", "Boston"};

//   // Add new record
//   rows.push_back(newRecord);

//   // Write updated CSV
//   ofstream outfile("data.csv");

//   for(auto row : rows) {
//     for(auto field : row) {
//       outfile << field << ",";
//     }
//     outfile << "\n";
//   }

//   outfile.close();


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

vector<vector<string>> rows;

int main() {
  ifstream infile("../tests/watched.csv");

  // Read CSV into rows
  string line;
  while(getline(infile, line)) {
    vector<string> row;

    string field;
    stringstream ss(line);

    while(getline(ss, field, ',')) {
      row.push_back(field);
    }

    rows.push_back(row);
  }
  std::cout <<  rows.size() << std::endl;
  std::cout << rows[0][3] << std::endl;
  std::cout << rows[1][1] << std::endl;
  std::cout << rows[1][3] << std::endl;

  return 0;
}

*/