class Solution {

    private PriorityQueue<Integer> maxheap;

    public int lastStoneWeight(int[] stones) {
        
        this.maxheap = new PriorityQueue<Integer>((a, b) -> b - a);

        for (int stone : stones){
            maxheap.offer(stone);
        }

        while (maxheap.size() > 1){
            int a = maxheap.poll();
            int b = maxheap.poll();
            int result = a-b;
            if(result!=0){
                maxheap.offer(result);
            }
        }
        if (maxheap.size()>0){
            return maxheap.poll();
        }
        return 0;

    }
}
