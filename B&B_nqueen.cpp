#include <iostream>
using namespace std;

#define N 4

int board[N][N];

bool leftRow[N];
bool upperDiagonal[2*N-1];
bool lowerDiagonal[2*N-1];

bool solve(int col)
{
    if(col >= N)
        return true;

    for(int row = 0; row < N; row++)
    {
        if(leftRow[row] == 0 &&
           lowerDiagonal[row + col] == 0 &&
           upperDiagonal[N - 1 + col - row] == 0)
        {
            board[row][col] = 1;

            leftRow[row] = true;
            lowerDiagonal[row + col] = true;
            upperDiagonal[N - 1 + col - row] = true;

            if(solve(col + 1))
                return true;

            // Backtrack
            board[row][col] = 0;

            leftRow[row] = false;
            lowerDiagonal[row + col] = false;
            upperDiagonal[N - 1 + col - row] = false;
        }
    }

    return false;
}

void printBoard()
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
            cout << board[i][j] << " ";

        cout << endl;
    }
}

int main()
{
    if(solve(0))
        printBoard();
    else
        cout << "No solution";

    return 0;
}