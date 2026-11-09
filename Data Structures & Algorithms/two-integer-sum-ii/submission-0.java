class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l=numbers.length;
        for(int i=0;i<l;i++){
            for(int j=i+1;j<l;j++){
                int x=numbers[i]+numbers[j];
                if(x==target)
                return new int[]{i+1,j+1};
                else if(x>target)
                break;
            }
        }
        return new int[]{-1,-1};
    }
}
