class Solution {
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    sortColors(nums) {
        let low=0,high=nums.length-1,mid=0;
        while(mid<=high){
            if(nums[mid]==1)
            mid+=1;
            else if(nums[mid]==0){
                [nums[mid],nums[low]]=[nums[low],nums[mid]];
                mid+=1;
                low+=1;
            }
            else{
                [nums[mid],nums[high]]=[nums[high],nums[mid]];
                high-=1;
            }
        }
        return nums;
    }
}
