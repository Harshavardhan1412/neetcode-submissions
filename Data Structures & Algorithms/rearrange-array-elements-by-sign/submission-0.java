class Solution {
    public int[] rearrangeArray(int[] nums) {
        List<Integer> pos=new ArrayList<>();
        List<Integer> neg=new ArrayList<>();
        int n=nums.length;
        int[] res=new int[n];
        for(int i=0;i<n;i++){
            if(nums[i]<0){
                neg.add(nums[i]);
            }
            else{
                pos.add(nums[i]);
            }
        }
        for(int i=0;i<pos.size();i++){
            res[2*i]=pos.get(i);
        }
        for(int i=0;i<pos.size();i++){
            res[2*i+1]=neg.get(i);
        }
        return res;
    }
}