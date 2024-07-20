#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

#include "csv_parser.h"

std::vector<std::vector<std::string>> read_csv(std::string filepath)
{
    std::ifstream file;
    file.open(filepath);
    std::string line;
    int counter;
    getline(file, line);

    std::vector<std::vector<std::string>> rows;
    while (getline(file, line))
    {
        std::vector<std::string> row;
        counter = 0;
        std::string field;
        std::stringstream ss(line);

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
    file.close();
    return rows;
}