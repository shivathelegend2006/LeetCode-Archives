#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes) {
    int n = matSize,m = matColSize[0];
    if (m*n != r*c){
     *returnSize = n;
    *returnColumnSizes = matColSize;
        return mat;
    }
    *returnSize = r;
    *returnColumnSizes = (int*)malloc(r*sizeof(int));
    for(int i=0;i<r;i++)
        (*returnColumnSizes)[i]= c;
    int **newMat = (int**)malloc(r*sizeof(int*));
    for (int i=0;i<r;i++)
        newMat[i] = (int*)malloc(c*sizeof(int));
    int p=0, q=0;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            newMat[i][j] = mat[p][q++];   
            if (q == m){
                q = 0;
                p++;
            }
        }
    
    }
    return newMat;
}