bool divideArray(int* nums, int numsSize) {
    int count[501] = {0}; // Using 501 since nums[i] can range from 1 to 500
    
    // Count the occurrences of each number in nums
    for (int i = 0; i < numsSize; ++i) {
        count[nums[i]]++;
    }
    
    // Check if each number appears even number of times
    for (int i = 1; i <= 500; ++i) {
        if (count[i] % 2 != 0) {
            return false;
        }
    }
    
    return true;
}