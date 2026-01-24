#include <stdlib.h>

void merge(int *arr, int left, int mid, int right){
    int n1 = mid - left +1;
    int n2 = right - mid;
    int i,j ,k;
    int L[n1], R[n2];
    for(int i=0;i<n1;i++)
        L[i] = arr[left +i];
    for(int i=0;i<n2;i++)
        R[i] = arr[mid + 1+i];
    i = 0, j=0; k=left;
    while (i< n1 && j< n2){
        if (L[i] < R[j]){
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i< n1){
        arr[k] = L[i];
        k++;
        i++;
    }
    while (j<n2){
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int *arr, int left, int right){
    if (left < right){
        int mid = left + (right - left) /2;
        mergeSort(arr,left,mid);
        mergeSort(arr,mid+1,right);
        merge(arr,left,mid,right);
    }
}
int minPairSum(int* nums, int numsSize){
    int n = numsSize;
    mergeSort(nums,0,n-1);
    for(int i =0;i<n/2;i++){
        nums[i] = nums[i] + nums[n-1-i];
    }
    int max = nums[0];
    for(int i=0;i<n;i++){
        if (nums[i] > max)
            max = nums[i];
    }
    return max;
}