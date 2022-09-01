/*
#Bryce W Frazier 2022/8/20


# Output After 1 Billon Cycles:
#   ~$ python3 ~/Code/montyHall.py
#   Keep win: 33.3333156%
#   Switch win: 66.6666844%
#   Runtime: 2261.917884349823
*/
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <time.h>


int main(){

  //random seed
  srand(time(NULL));

  //Point vars
  long double keepWin = 0;
  long double switchWin = 0;
  int codeIsZonk = 0;

  // Number of games
  int loopCount = 2147483647;

  //Set start time
  // Time is long to midigate 2038
  long int startTime = time(NULL);

  //main loop
  for(int i = loopCount; i > 0; i--){


    //get win and selected doors
    int win = rand() % 3 + 1;
    int select = rand() % 3 + 1;
    int altSelect = 0;
    int opened;

    // select opened door
    if((win == 1 || win == 2) & (select == 1 || select == 2)){
      opened = 3;
    }
    if((win == 1 || win == 3) & (select == 1 || select == 3)){
      opened = 2;
    }
    if((win == 2 || win == 3) & (select == 2 || select == 3)){
      opened = 1;
    }

    //get altSelect
    if((opened == 1 || opened == 2) & (select == 1 || select == 2)){
      altSelect = 3;
    }
    if((opened == 1 || opened == 3) & (select == 1 || select == 3)){
      altSelect = 2;
    }
    if((opened == 2 || opened == 3) & (select == 2 || select == 3)){
      altSelect = 1;
    }

    //count wins
    if(select == win){
      keepWin += 1;
    } else if (altSelect == win){
      switchWin += 1;
    } else {
      codeIsZonk += 1;
    }


  }
  // get end and runtime
  long int endTime = time(NULL);
  long int runTime = endTime - startTime;

  // print output
  int total = keepWin + switchWin + codeIsZonk;
  printf("%s%Lf%s\n", "Stay win: ", keepWin/total*100, "%");
  printf("%s%Lf%s\n", "Switch win: ", switchWin/total*100, "%");
  printf("Run time: %ld\n", runTime);
  printf("\n");

  if(codeIsZonk != 0){
    printf("This program is a zonk!: Missing data points\n");
    printf("Missing data: %d\n", codeIsZonk);
  }
  if(keepWin/total + switchWin/total!= 1){
    printf("This run maybe a zonk!: Rounding Error\n");
    printf("Total offset: %Lf\n", keepWin+switchWin);
  }

 return 0;
}
