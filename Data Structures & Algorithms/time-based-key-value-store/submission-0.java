class TimeMap {

    private HashMap<String,HashMap<Integer,String>> map;

    public TimeMap() {
        this.map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new HashMap<>()).put(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        HashMap<Integer,String> currentMap = map.get(key);
        if (currentMap==null){
            return "";
        }
        if(currentMap.containsKey(timestamp)){
            return currentMap.get(timestamp);
        }
        else{
            Integer[] keys = currentMap.keySet().toArray(new Integer[0]);
            Arrays.sort(keys);
            int prev = -1;
            int i = 0;
            for(int time : keys){
                if(time>timestamp){
                    break;
                }
                prev = time;
            }
            if (prev == -1){
                return "";
            }
            return currentMap.get(prev);

        }
    }
}
