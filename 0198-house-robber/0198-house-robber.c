int rob(int* nums, int numsSize) {
    int max1 = 0;
    int max2 = 0;
    for(int i=0;i<numsSize;i++){
        int curr = (nums[i] + max1 > max2) ? (nums[i]+max1) : max2;
        max1 = max2;
        max2 = curr;
    }
    return max2;
}