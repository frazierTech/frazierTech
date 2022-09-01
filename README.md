  montyHall.o allows the user to simulate the montyHall problem 2,147,483,647 times and the program will display
long double values of the percentage of winning by staying at the inital selected door vs switching.
  superMontyHall.o in addition
 to simulating the problem 100,000,000 times it also runs a montyHall scenairo with 100
doors and Monty opens 98 zonk doors.

In the precompiled files int loopCount can be changed to set the number of times the montyHall simulation is 
repeated.
In superMontyHall.c there is another variable int doorNum the effects the number of doors in game.

It is recomended that int doorNum is at least 3 and int loopCount is as high as practicaly posable so there is a 
good sample size. (My computer can run the maxuim number(2147483647) that the int data type can hold)
