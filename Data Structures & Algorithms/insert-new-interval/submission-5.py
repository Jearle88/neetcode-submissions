class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #while itrating through, merger any merge any existing overlapping intervals
        # if the new interval fits into a new merged interval, then we mergeit and return
        # if it does not, we keep itrarting until we find the place on the list where it should be
        #that 

        intervals.append(newInterval)
        intervals.sort()
       # n=len(intervals)
       # new_on0
        i=0
        while i< len(intervals):
            if i+1<len(intervals) and intervals[i][1]>=intervals[i+1][0]:
                intervals[i][1]=max(intervals[i+1][1],intervals[i][1])
                intervals.pop(i+1)
            else:
                i+=1
        return intervals
    
      