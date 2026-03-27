bool canJump(int* nums, int numsSize) {
    
    int i=0;

        int farthest = 0;
        for(int i=0;i<numsSize;i++){
            if(i > farthest) return false;
            if(nums[i] + i > farthest) farthest = nums[i] +i;
            if(farthest >= numsSize - 1) return true;
        }

    return true;
}