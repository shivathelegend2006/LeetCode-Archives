void dfs(char** grid, int gridSize, int*gridColSize,int r, int c){
    if (c <0 || r<0 || r >= gridSize  || c >= gridColSize[r] || grid[r][c] == '0' ) return;
    grid[r][c] = '0';
    dfs(grid,gridSize, gridColSize, r-1,c); //up
    dfs(grid,gridSize, gridColSize, r+1,c); //down    
    dfs(grid,gridSize, gridColSize, r,c+1); //right    
    dfs(grid,gridSize, gridColSize, r,c-1); //left    
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int count = 0;
    for(int i=0;i<gridSize;i++){
        for(int j=0;j<gridColSize[i] ; j++){
            if(grid[i][j]=='1'){
                count++;
                dfs(grid,gridSize,gridColSize,i,j);
            }
        }
    }
    return count;
}