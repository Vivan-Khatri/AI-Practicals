//CSP N Queens Problem
#include <iostream>
using namespace std;

#define N 4

int board[N][N];

// Function to print solution
void printBoard()
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
            cout << board[i][j] << " ";

        cout << endl;
    }
}

// Check whether queen can be placed
bool isSafe(int row, int col)
{
    int i, j;

    // Check left side
    for(i = 0; i < col; i++)
        if(board[row][i])
            return false;

    // Upper diagonal
    for(i=row, j=col; i>=0 && j>=0; i--, j--)
        if(board[i][j])
            return false;

    // Lower diagonal
    for(i=row, j=col; j>=0 && i<N; i++, j--)
        if(board[i][j])
            return false;

    return true;
}

// Backtracking function
bool solveNQ(int col)
{
    // All queens placed
    if(col >= N)
        return true;

    for(int i = 0; i < N; i++)
    {
        if(isSafe(i, col))
        {
            board[i][col] = 1;

            if(solveNQ(col + 1))
                return true;

            // BACKTRACK
            board[i][col] = 0;
        }
    }

    return false;
}

int main()
{
    if(solveNQ(0) == false)
    {
        cout << "Solution does not exist";
        return 0;
    }

    printBoard();

    return 0;
}   