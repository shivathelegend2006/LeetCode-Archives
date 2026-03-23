int maxProduct(int* nums, int numsSize) {
    int n = numsSize;
    double maxPro = nums[0];
    double pre = 1, post = 1;
    for(int i=0;i<n;i++){
        if(pre == 0) pre = 1;
        if (post == 0) post = 1;

        pre *= nums[i];
        post *= nums[n-1-i];

        if(pre > maxPro) maxPro = pre;
        if(post > maxPro) maxPro = post;
    }
    return (int) maxPro;
}