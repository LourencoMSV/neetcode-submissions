class Solution {

    private int distance(int[] point){

        return point[0]*point[0]+point[1]*point[1];
    }

    public int[][] kClosest(int[][] points, int k) {
        
        PriorityQueue<int[]> heap = new PriorityQueue<>((a,b)-> Integer.compare(distance(a), distance(b)));

        for (int[] point : points){
            heap.offer(point);
        }

        int[][] result = new int[k][2];

        for (int i=0; i<k;i++){
            result[i]= heap.poll();
        }
        return result;
    }
}
