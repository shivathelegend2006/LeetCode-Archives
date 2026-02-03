int maxArea(int* height, int heightSize) {
    int n = heightSize;
    int i =0,j = n-1,maxArea = 0;
    while (i < n && j >= 0){
        int min = height[j];
        if (height[j]>height[i])
            min = height[i];
        int area = (j-i)*min;
        if (area>maxArea)
            maxArea = area;
            if (min == height[j])
                j--;
            else 
                i++;
        if (j==i)
            break;
        
    }
    return maxArea;
}