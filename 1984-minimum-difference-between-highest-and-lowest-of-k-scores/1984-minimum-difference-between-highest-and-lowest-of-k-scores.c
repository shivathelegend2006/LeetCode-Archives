#include <stdlib.h>

void insertionSort(int *arr, int n){
    int i, j, key;
    for(i=1;i<n;i++){
        key = arr[i];
        j = i-1;
        while (j>=0 && arr[j]>key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

int minimumDifference(int* nums, int numsSize, int k) {
    int n = numsSize;

    insertionSort(nums,n);
    int minSum = 1000;
    if (n == 1)
        return 0;
    else 
        minSum = nums[n-1] - nums[0];

    for (int i = 0;i<=n-k;i++){
        int diff = abs(nums[i+k-1]-nums[i]);
        if (diff < minSum)
            minSum = diff;
    }
    return minSum;

}