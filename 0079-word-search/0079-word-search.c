//instanstaly recognise that we execute dfs
bool dfs(char** board, int boardSize, int* boardColSize, char* word, int i, int j, int index){
    if (word[index] == '\0') return true;

    if (i < 0 || i >= boardSize || j < 0 || j >= boardColSize[i] || board[i][j] != word[index]) {
        return false;
    }

    char temp = board[i][j];
    board[i][j] = '*';
    bool found = dfs(board, boardSize, boardColSize, word, i+1, j, index+1) || dfs(board, boardSize, boardColSize, word, i-1, j, index +1) || dfs(board, boardSize, boardColSize, word, i, j+1, index + 1) || dfs(board, boardSize, boardColSize, word, i, j-1, index +1);
    board[i][j] = temp;
    return found;
}

bool exist(char** board, int boardSize, int* boardColSize, char* word) {
    for(int i=0;i<boardSize; i++){
        for(int j=0;j< boardColSize[i] ; j++){
            if(board[i][j] == word[0]){
                if (dfs(board, boardSize, boardColSize, word, i, j, 0)) return true;
            }
        }
    }
    return false;
}