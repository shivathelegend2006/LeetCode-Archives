/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

void backtrack(int* candidates, int n, int target, int index,
               int* currentCombo, int currentLen,
               int** result, int* returnSize, int** returnColumnSizes) {
    if (target == 0) {
        result[*returnSize] = (int*)malloc(currentLen * sizeof(int));
        for (int i = 0; i < currentLen; i++) {
            result[*returnSize][i] = currentCombo[i];
        }
        (*returnColumnSizes)[*returnSize] = currentLen;
        (*returnSize)++;
        return;
    }

    if (target < 0 || index >= n) {
        return;
    }

    currentCombo[currentLen] = candidates[index];
    backtrack(candidates, n, target - candidates[index], index,
              currentCombo, currentLen + 1, result, returnSize, returnColumnSizes);

    backtrack(candidates, n, target, index + 1,
              currentCombo, currentLen, result, returnSize, returnColumnSizes);
}

int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {
    int n = candidatesSize;
    int max_combos = 150;
    int** result = (int**)malloc(max_combos * sizeof(int*));
    *returnColumnSizes = (int*)malloc(max_combos * sizeof(int));
    *returnSize = 0;

    int* currentCombo = (int*)malloc(50 * sizeof(int));

    backtrack(candidates, n, target, 0, currentCombo, 0, result, returnSize, returnColumnSizes);

    free(currentCombo);

    return result;
}