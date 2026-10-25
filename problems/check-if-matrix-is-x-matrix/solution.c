bool checkXMatrix(int** grid, int gridSize, int* gridColSize) {
    int n=gridSize;
    for (int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if ((i==j && grid[i][j]==0) || ((i+j==n-1) && grid[i][j]==0) ){
                return false;
            }
            if (grid[i][j]!=0 && i!=j && i+j!=n-1){
                return false;
            }
        }
    }
    return true;
}