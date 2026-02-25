// 1. The helper function that teaches qsort how to compare two numbers
int compare(const void *a, const void *b) {
    int int_a = *(int*)a;
    int int_b = *(int*)b;
    // We do this instead of (a - b) to prevent huge numbers from overflowing!
    if (int_a < int_b) return -1;
    if (int_a > int_b) return 1;
    return 0;
}

bool containsDuplicate(int* nums, int numsSize) {
    // 2. Sort the array
    qsort(nums, numsSize, sizeof(int), compare);
    
    // 3. Walk the line and check neighbors
    // We stop at numsSize - 1 so we don't check past the end of the array!
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            return true; // Duplicate found!
        }
    }
    
    return false; // Clean array, no duplicates.
}