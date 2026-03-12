int removeElement(int* nums, int numsSize, int val) {
    int n = numsSize;
    int k = 0;
    for(int i=0;i<n;i++){
        if (nums[i] != val){ 
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}