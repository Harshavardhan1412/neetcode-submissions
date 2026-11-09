class Solution {
    public int maxSubArray(int[] nums) {
        int sum=nums[0],ma=nums[0];
        for(int i=1;i<nums.length;i++){
            sum=Math.max(nums[i],nums[i]+sum);
            ma=Math.max(sum,ma);
        }
        ma=Math.max(sum,ma);
        return ma;
    }
}
