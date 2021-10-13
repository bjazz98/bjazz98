#include "Functions.h"
#include <iostream>
using namespace std;
void runGame()
{
    int x;
    int y;
    char value;
    char board[3][3];
    char turn = 'X';
    char again = true;
    while (again){
        char turn = 'X';
        initBoard(board);
        while (checkForWinner(turn,board)==false&&checkForDraw(board)==false){
            cout<<"Enter coordinate for "<<turn<<". Input should be X Y"<<endl;
            cin>>x>>y;
            placeAPiece(x,y,turn,board);
            displayBoard(board);
            if(checkForWinner(turn,board)){
                cout<<turn<<" Won"<<endl;
                cout<<"Do you want to play again?"<<endl;
                cin>>value;
                if (value == 'Y'||value == 'y'){
                    again = true;
                    break;
                }
                else if (value == 'N'||value == 'n'){
                    again = false;
                    cout<<"Done"<<endl;
                    break;
                }

            }
            else if(checkForDraw(board)){
                cout<<"Draw"<<endl;
                cout<<"Do you want to play again?"<<endl;
                cin>>value;
                if (value == 'Y'||value == 'y'){
                    again = true;
                    break;
                }
                else if (value == 'N'||value =='n'){
                    again = false;
                    cout<<"Done"<<endl;
                    break;
                }
            }
            if(turn == 'X'){
                turn = 'O';
            }
            else{
                turn = 'X';
            }



            }

        }
}

void initBoard(char board[3][3])
{
//creates 3x3 tic tac toe board with no pieces
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            board[i][j] = '-';
}
    }
}

void placeAPiece(int x, int y, char piece, char board[3][3])
{
//places piece on the board by given index 
    if(board[x][y] == '-'){
        board[x][y] = piece;
    }

}

bool checkForWinner(char piece, char board[3][3])
{
    //checks if board has winner horizantally 
    for(int i =0;i<3;i++){
        if((board[i][0] == board[i][1]) && (board[i][1] == board[i][2])){
            if(board[i][0] == piece){
                return true;
            }
        }
        if((board[0][i] == board[1][i]) && (board[1][i] == board[2][i])){
            if(board[0][i] == piece){
                return true;
            }
            }
        }
    //checks if board has winner diagonally 
    if((board[0][0] == board[1][1]) && (board[1][1] == board[2][2])){
        if(board[0][0]== piece){
            return true;
        }
    }
        else if((board[0][2] == board[1][1]) && (board[1][1] == board[2][0])){
            if(board[0][2] == piece){
                return true;
            }
        }
    return false;
}


bool checkForDraw(char board[3][3])
{   //checks if there's a draw by checking if all the pieces all placed and check for winner was not called
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if (board[i][j] != 'X' && board[i][j] != 'O')
            {
                return false;
            }
        }
    }
    return true;
}

void displayBoard(char board[3][3])
//displays the physical board on the console
{
    for(int i =0;i<3;i++){
        for(int j=0;j<3;j++){
            if(j != 2){
                cout<<""<<board[i][j]<<"|";
            }
            else{
                cout<<""<<board[i][j];
            }
        }
        if (i != 2){
            cout<<endl<<"-----"<<endl;
        }
        else{
            cout<<endl;
        }
        }

    }
