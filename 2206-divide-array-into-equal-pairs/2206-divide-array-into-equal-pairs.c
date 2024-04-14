




bool divideArray(int* nums, int numsSize) {
    int freq[501] = {0}; // Assuming the maximum value of nums[i] is 500
    
    // Count occurrences of each number
    for (int i = 0; i < numsSize; ++i) {
        freq[nums[i]]++;
    }
    
    // Check if each number has even frequency
    for (int i = 1; i <= 500; ++i) {
        if (freq[i] % 2 != 0) {
            // If any number has odd frequency, cannot form pairs
            return false;
        }
    }
    
    // All numbers have even frequency, can form pairs
    return true;
}