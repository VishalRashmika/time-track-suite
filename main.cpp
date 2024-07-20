#include <iostream>
#include "include/request.h"
#include "include/letterboxd.h"
#include "include/csv_parser.h"
#include <vector>

int main(){
    Requests request;
    Letterboxd Letterboxd;
    CSV_parser parser; 

    std::vector<std::vector<std::string>> data;
    std::string filepath {"../tests/wathched.csv"};

    // std::cout << parser.read_csv(filepath).size() <<std::endl;


    std::cout << "awdawd" << std::endl;

    std::string url {"https://letterboxd.com/film/hit-man-2023/"};
    //std::cout << request.Get(url) << std::endl;

    std::cout << "e4te4tet" << std::endl;

    int time;
    time = Letterboxd.get_time(request.Get(url));

    std::cout << time << std::endl;


    return 0;
}

/*
g++ -std=c++17  main.cpp ./include/request.cpp -lcurl ./include/request.h ./include/letterboxd.h ./include/letterboxd.cpp -lgumbo -o main && ./main
*/