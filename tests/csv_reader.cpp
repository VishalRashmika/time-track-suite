#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

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

int main(){

    std::string filepath {"../include/watched.csv"};

    std::vector<std::vector<std::string>> rows;
    rows = read_csv(filepath);

    std::cout << rows.size() << std::endl;
    for (int i = 0; i < rows.size() - 1; i++){
        for (int j = 0; j < 2; j++){
            std::cout << rows[i][j] << std::endl;
        }
    }
    return 0;
}