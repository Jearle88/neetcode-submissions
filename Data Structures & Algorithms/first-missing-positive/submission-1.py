class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        n=len(nums)
        count=1
        prev=1
        for i in range(n):
            if nums[i]<1:
                continue
            if nums[i]==count:
                count+=1
                prev=nums[i]
            elif nums[i]==prev:
                continue
            else:
                print(i)
                return count
        return count