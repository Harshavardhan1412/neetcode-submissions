class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result=new ArrayList<>();
        for(int i=0;i<numRows;i++){
            int num=1;
            List<Integer> res=new ArrayList<>();
            for(int j=0;j<=i;j++){
                res.add(num);
                num=num*(i-j)/(j+1);
            }
            result.add(res);
        }
        return result;
    }
}