#include <iostream>  
#include <fstream>  
#include <string>  
#include <vector>  
#include <sstream>
using namespace std;  
  
int main() {  
  
  ifstream infile("report_card.csv");  
  vector<vector<string>> rows;  
  
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
  std::cout << rows[0][0] << std::endl;
  std::cout << rows[1][0] << std::endl;
  std::cout << rows[0][1] << std::endl;
  std::cout << rows[1][1] << std::endl;
  
  return 0;  
} 

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
*/