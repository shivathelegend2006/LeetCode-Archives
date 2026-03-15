int searchInsert(int* nums, int numsSize, int target) {
    int upper, lower, mid;
    int n = numsSize;
    upper = n-1;
    lower = 0;
    while(lower <= upper){
        mid = (upper + lower)/2;
        if(target > nums[mid])
            lower = mid+1;
        else if (target < nums[mid]) upper = mid-1;
        else 
            return mid;
    }
    return lower;
}