int maxProfit(int* prices, int pricesSize) {
    int n = pricesSize;
    int i,j;
    int profit = 0;
    int max = prices[0];
    for (i=0;i<n;i++){
        if (prices[i]> max)
            max = prices[i];
    }
    int min = max;
    for (i=0;i<n;i++){
        if (prices[i]<min)
            min = prices[i];
        else {
            if (prices[i] - min > profit)
                profit = prices[i] - min; 
        }
    }
    return profit;
}