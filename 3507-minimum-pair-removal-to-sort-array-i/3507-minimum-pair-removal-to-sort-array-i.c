int minimumPairRemoval(int* nums, int numsSize) {
    int cond=0,steps = 0;
    int numSize = numsSize;
    while (cond == 0){
        cond =1;
        for(int i=0;i<numSize-1;i++){
            if (nums[i+1]< nums[i]){
                cond = 0;
                break;
            }
        }
        if (cond == 1)
            return steps;
        int i=0,sum=nums[0] + nums[1];
    
        for(int j=0;j<numSize-1;j++){
            if (nums[j]+ nums[j+1] < sum){
                sum = nums[j] + nums[j+1];
                i = j;
            }
        }
        nums[i] = sum;
        for(int j=i+1;j<numSize-1;j++)
            nums[j] = nums[j+1];
        steps++;
        numSize--;
    }   
    return steps;
}
