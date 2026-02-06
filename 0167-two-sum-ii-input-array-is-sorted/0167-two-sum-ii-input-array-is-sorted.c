/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include <stdlib.h>
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int n = numbersSize;
    int i = 0,j = n-1;
    int *index = (int*)malloc(2*sizeof(int));
    *returnSize = 2;
    while(i<j){
        int sum = numbers[i] + numbers[j];
        if (sum == target){
            index[0] = i+1;
            index[1] = j+1;
            break;
        }         
        else if(sum > target)
            j--;
        else
            i++;
    }
    return index;
}