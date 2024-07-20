#include <iostream>
#include "include/request.h"
#include "include/letterboxd.h"
#include "include/csv_parser.h"

int main(){
    Requests request;
    Letterboxd Letterboxd;
    CSV_parser csv_parser; 

    vector<vector<std::string>> data;
    std::string filepath {"./tests/wathched.csv"};

    data = csv_parser.read_csv(filepath);

    std::string url {"https://letterboxd.com/film/hit-man-2023/"};
    //std::cout << request.Get(url) << std::endl;

    int time;
    time = Letterboxd.get_time(request.Get(url));

    std::cout << time << std::endl;


    return 0;
}

/*
g++ -std=c++17  main.cpp ./include/request.cpp -lcurl ./include/request.h ./include/letterboxd.h ./include/letterboxd.cpp -lgumbo -o main && ./main
*/