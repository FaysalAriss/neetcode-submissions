class Solution {
    public static class Pair{
        public int position;
        public int speed;
        public Pair(int position, int speed){
            this.position = position;
            this.speed = speed;
        }
    }

    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        if(n == 0) { return 0; }
        int fleetsDone = 0;
        Pair[] pairs = new Pair[n];

        for(int i = 0; i < n; i++){
            pairs[i] = new Pair(position[i], speed[i]);
        }

        Arrays.sort(pairs, Comparator.comparingInt((Pair p) -> p.position).reversed());
        float[] time = new float[n]; //how long each needs until the end

        for(int i = 0; i < n; i++){
            time[i] = (target-pairs[i].position)/(float)pairs[i].speed;
        }
        for(int i = 1; i < n; i++){
            time[i] = Math.max(time[i-1], time[i]);
        }


        
        //count distinct sequences
        int i = 0;
        float current = time[i];
        while(i < n){
            current = time[i];
            while(i < n && time[i] == current){
                i++;
            }
            fleetsDone++;
        }

        return fleetsDone;
    }

}
