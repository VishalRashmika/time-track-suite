
main: main.o letterboxd.o request.o
	g++ main.o letterboxd.o -lgumbo request.o  -lcurl -o main
	rm *.o

main.o: main.cpp
	g++ -c main.cpp -lgumbo -lcurl

letterboxd.o: ./include/letterboxd.cpp ./include/letterboxd.h
	g++ -c  ./include/letterboxd.cpp 

request.o: ./include/request.cpp ./include/request.h
	g++ -c ./include/request.cpp 

clean: 
	rm main

run:
	./main