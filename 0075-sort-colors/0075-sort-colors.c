void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sortColors(int* nums, int numsSize) {
//using the dutch national flag algorithm
    int high = numsSize -1, low = 0, mid = 0;
    while(mid <= high){
        int n = nums[mid];
        if(n == 0){
            swap(&nums[mid], &nums[low]);
            mid++;
            low++;
        }
        else if (n==2){
            swap(&nums[mid], &nums[high]);
            high--;
        }
        else mid++;
    }
}