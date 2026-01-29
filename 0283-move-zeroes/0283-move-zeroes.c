void moveZeroes(int* nums, int numsSize) {
    int n = numsSize;
    int i,p=0;
    for (i=0;i<n;i++){
        if (nums[i] != 0){
            nums[p] = nums[i];
            p++;
        }
    }
    for(int i=p;i<n;i++)
        nums[i] = 0;
}