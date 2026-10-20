class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)        
        low=0
        high=n-1
        res=0
        while low<high:
            curr= min(heights[low],heights[high])*(high-low)
            res=max(res,curr)
            if heights[low]>heights[high]:
                high-=1
            else:
                low+=1
        return res