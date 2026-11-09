class Solution {
    public List<String> stringMatching(String[] words) {
        Set<String> res=new HashSet<>();
        Arrays.sort(words,(a,b)->a.length()-b.length());
        for(int i=0;i<words.length;i++){
            for(int j=i+1;j<words.length;j++){
                if(words[j].contains(words[i])){
                    res.add(words[i]);
                }
            }
        }
        return new ArrayList<>(res);
    }
}