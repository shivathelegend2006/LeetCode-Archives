int search(int* nums, int numsSize, int target) {
    int lower, upper,mid;
    upper = numsSize - 1;
    lower = 0;
    while(lower <= upper){
        mid = (lower+upper)/2;
        if(target == nums[mid]) return mid;

        if(nums[lower] <= nums[mid]){
            if(target >= nums[lower] && target <= nums[mid])
                upper = mid-1;
            else lower = mid+1;
        }
        else {
            if (nums[upper] >= target && target > nums[mid])
                lower = mid + 1;
            else 
                upper = mid -1;
        }
    }
    return -1;
}