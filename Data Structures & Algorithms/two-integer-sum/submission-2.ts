class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {

        for(let i=0; i<nums.length; i++){
            let curr_comp=target-nums[i];
   
            
            for(let j=0; j<nums.length; j++){
                 if (i!==j){
                    
                if (nums[j]+nums[i]==target){
                    
                     return [i,j];

                }

            }

            }  
           
        }

    }
}
