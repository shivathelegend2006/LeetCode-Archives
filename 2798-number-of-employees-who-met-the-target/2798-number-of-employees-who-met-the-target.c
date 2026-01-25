int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target) {
    int n = hoursSize;
    int count = 0;
    for (int i=0;i<n;i++){
        if (hours[i] >= target)
            count++;
    }
    return count;
}