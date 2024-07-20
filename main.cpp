// #include <iostream>
// #include <vector>
// #include <fstream>
// #include <string>
// #include <sstream>

// #include "include/request.h"
// #include "include/letterboxd.h"

// std::vector<std::vector<std::string>> rows;

// std::vector<std::vector<std::string>> read_csv(std::string filepath){
//     std::ifstream file;
//     file.open(filepath);
//     std::string line;
//     int counter;
//     getline(file, line);

//     while (getline(file, line))
//     {
//         std::vector<std::string> row;
//         counter = 0;
//         std::string field;
//         std::stringstream ss(line);

//         while (getline(ss, field, ','))
//         {
//             if (counter == 1 || counter == 3)
//             {
//                 row.push_back(field);
//             }
//             counter += 1;
//         }
//         rows.push_back(row);
//     }
//     file.close();
//     return rows;
// }

// int main(){
//     Requests request;
//     Letterboxd Letterboxd;

//     std::string filepath {"./tests/wathched.csv"};
//     std::vector<std::vector<std::string>> data;
//     data = read_csv(filepath);
//     std::cout << data.size() <<std::endl;


//     std::string location {"./watched.csv"};
//     std::vector<std::vector<std::string>> rows;
//     rows = read_csv(filepath); 
//     std::cout << "ROWS : " << rows.size() << std::endl;
//     // for (int i = 0; i < rows.size() - 1; i++){
//     //     for (int j = 0; j < 2; j++){
//     //         std::cout << rows[i][j] << std::endl;
//     //     }
//     // }

//     std::string url {"https://letterboxd.com/film/hit-man-2023/"};
//     //std::cout << request.Get(url) << std::endl;

//     int time;
//     time = Letterboxd.get_time(request.Get(url));

//     std::cout << time << std::endl;


//     return 0;
// }





// /*
// g++ -std=c++17  main.cpp ./include/request.cpp -lcurl ./include/request.h ./include/letterboxd.h ./include/letterboxd.cpp -lgumbo -o main && ./main
// */






#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

#include "include/request.h"
#include "include/letterboxd.h"
#include "include/csv_parser.h"

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

    std::string filepath {"./tests/watched.csv"};

    std::vector<std::vector<std::string>> rows;
    rows = read_csv(filepath);
    std::cout << rows.size() << std::endl;
    for (int i = 0; i < rows.size(); i++){
        for (int j = 0; j < 2; j++){
            std::cout << rows[i][j] << std::endl;
        }
    }

    Requests request;
    Letterboxd Letterboxd;

    std::string url {"https://letterboxd.com/film/hit-man-2023/"};
    //std::cout << request.Get(url) << std::endl;

    int time;
    time = Letterboxd.get_time(request.Get(url));

    std::cout << time << std::endl;

    return 0;
}