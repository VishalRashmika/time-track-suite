#include <iostream>  
#include <fstream>  
#include <string>  
#include <vector>  
#include <sstream>

#include "csv_parser.h"

using namespace std;  
  
vector<vector<string>> rows;  

vector<vector<string>> CSV_parser::read_csv(std::string filepath) {    
  ifstream infile(filepath);  
  
  // Read CSV into rows  
  string line;
  int counter;   
  while(getline(infile, line)) {  
    vector<string> row;
    counter = 0;
    string field;  
    stringstream ss(line);  
    
    while(getline(ss, field, ',')) { 
        if (counter == 1 || counter == 3){
            row.push_back(field);
        }
        counter += 1;
    }  
    rows.push_back(row);  
  }  
  std::cout <<  rows.size() << std::endl;
  std::cout << rows[0][0] << std::endl;
  std::cout << rows[0][1] << std::endl;

  std::cout << rows[1][0] << std::endl;
  std::cout << rows[1][1] << std::endl;

  std::cout << rows[2][0] << std::endl;
  std::cout << rows[2][1] << std::endl;
  
  return rows;
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