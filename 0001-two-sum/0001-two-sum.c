/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include <stdlib.h>
int BinarySearch(int num[],int n, int target,int exclude){
    for(int i=0;i<n;i++){
        if (num[i]==target && i != exclude)
            return i;
    }
    return -1;
}
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int n = numsSize;
    *returnSize = 2;
    int *index = (int*)malloc(2*sizeof(int));
    for(int i=0;i<n;i++){
        int digit = target - nums[i];
        if (BinarySearch(nums,n,digit,i)!=-1){
            index[0] = i;
            index[1] = BinarySearch(nums,n,digit,i);
    }
    }
    return index;
}