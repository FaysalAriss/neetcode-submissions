class Solution {
    public int trap(int[] height) {
        int totalWater = 0;
        int left, right;
        left = 0;

        
        while(left < height.length && height[left] == 0){
            left++;
        }

        while(left < height.length - 1){ //if only one more space cannot trap water
            //found a bar
            right = left+1;
            int leftHeight = height[left];
            int sum = 0;
            while(right < height.length && height[right] < leftHeight){
                sum += height[right];
                right++;
            }
            if(right == height.length) {

                int initialLeft = left;
                right = height.length-1;
                while(right > initialLeft && height[right] == 0){
                    right--;
                }

                while(right > initialLeft){
                    left = right-1;
                    int rightHeight = height[right];
                    sum = 0;
                    while(left >= initialLeft && height[left] < rightHeight){
                        sum += height[left];
                        left--;
                    }
                    if(left < initialLeft) { return totalWater; }
                    totalWater += (right-left-1)*Math.min(height[left], rightHeight) - sum;
                    right = left;
                }

                return totalWater;
            }else{
                //found a bar of >= height
                totalWater += (right-left-1)*Math.min(leftHeight, height[right]) - sum;
                left = right;
            }
        }

        return totalWater;

        
    }

    //+6minutes
}
