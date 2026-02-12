int trap(int* height, int heightSize) {
    int n = heightSize;
    int rain = 0;
    if (n==1)
        return 0;
    int maxL[n],maxR[n];
    int mL = height[0];
    int mR = height[n-1];
    for(int i=0;i<n-1;i++){
        if (mL < height[i])
            mL = height[i];
        maxL[i] = mL;
    }
    for(int i = n-1;i>= 0;i--){
        if (mR < height[i])
            mR = height[i];
        maxR[i] = mR;
    }

    int i = 0;
    for (i = 1;i<n-1;i++){

        if (maxR[i] > height[i] && maxL[i] > height[i]){
            if (maxR[i] > maxL[i])
                rain += maxL[i] - height[i];
            else 
                rain += maxR[i] - height[i];
        }
    }
    return rain;
}