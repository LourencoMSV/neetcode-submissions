class Solution {
    public int leastInterval(char[] tasks, int n) {

        HashMap<Character, Integer> count = new HashMap<>();

        for(char c : tasks){
            if(count.containsKey(c)){
                count.replace(c,count.get(c)+1);
            }else {
                count.put(c,1);
            }
        }


        PriorityQueue<Integer> queue = new PriorityQueue<>((a, b) -> b - a);

        for(int v: count.values()){
            queue.add(v);
        }

        Queue<int[]> cooldownQueue = new LinkedList<>();
        int time = 0;

        while(queue.size()>0 || cooldownQueue.size()>0 ){
            time++;
            if (queue.isEmpty()){
                time = cooldownQueue.peek()[1];
            }else {
                int cnt = queue.poll()-1;
                if (cnt>0){
                    cooldownQueue.add(new int[]{cnt, time+n});
                }
            }
            if (!cooldownQueue.isEmpty() && cooldownQueue.peek()[1]==time){
                queue.add(cooldownQueue.poll()[0]);
            }
        }
        return time;

    }
}
