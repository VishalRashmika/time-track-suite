
main: main.o letterboxd.o request.o csv_parser.o
	g++ main.o csv_parser.o letterboxd.o -lgumbo request.o  -lcurl -o main
	rm *.o

main.o: main.cpp
	g++ -c main.cpp -lgumbo -lcurl

letterboxd.o: ./include/letterboxd.cpp ./include/letterboxd.h
	g++ -c  ./include/letterboxd.cpp 

request.o: ./include/request.cpp ./include/request.h
	g++ -c ./include/request.cpp 

csv_parser.o: ./include/csv_parser.cpp ./include/csv_parser.h
	g++ -c ./include/csv_parser.cpp

clean: 
	rm main

run:
	./main

commit:
	git add . && git commit && git push