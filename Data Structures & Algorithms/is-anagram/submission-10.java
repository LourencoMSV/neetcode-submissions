class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character,Integer> map = new HashMap<>();
        char[] chars_s = s.toCharArray();
        char[] chars_t = t.toCharArray();
        for(int i=0;i<chars_s.length;i++){
            if (map.containsKey(chars_s[i])){
                map.replace(chars_s[i],map.get(chars_s[i])+1);
            } else {
                map.put(chars_s[i],1);
            }
        }

        for(int i=0;i<chars_t.length;i++){
            if (map.containsKey(chars_t[i])){
                int new_value = map.get(chars_t[i])-1;
                if (new_value<0){
                    return false;
                }
                map.replace(chars_t[i],new_value);
            } else {
                return false;
            }
        }

        for(Character key : map.keySet()){
            if(map.get(key)>0){
                return false;
            }
        }
        return true;
    }
    
}
