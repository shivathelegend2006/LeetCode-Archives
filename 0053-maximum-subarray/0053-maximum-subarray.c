int sum(int arr[],int n){
    int sum = 0;
    for(int i=0;i<n;i++)
        sum += arr[i];
    return sum;
}
int maxSubArray(int* nums, int numsSize) {
    int n = numsSize;
    int maxSum = nums[0];
    int max = 0;
    int sum = 0;
    for(int i=1;i<n;i++){
        if (nums[i]<max)
            max = nums[i];
    }

    for(int i=0;i<n;i++){
        sum += nums[i];

        if (sum > maxSum)
            maxSum = sum;

        if (sum < 0)
            sum = 0;
        
    }

    return maxSum;
}