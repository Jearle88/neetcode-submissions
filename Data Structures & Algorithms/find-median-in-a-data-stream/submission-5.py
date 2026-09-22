import heapq


class MedianFinder:

    def __init__(self):
        
        self.stream=[]
        self.stream_len=0
       # heapq.heapify(stream)


    def addNum(self, num: int) -> None:

       # heapq.heappush(self.stream,num)
       self.stream.append(num)
       self.stream_len+=1
       self.stream.sort()
        

    def findMedian(self) -> float:
      
        res=-1
        heap_trash=[]
        if self.stream_len%2==0:
            res=(self.stream[(self.stream_len//2)] + self.stream[((self.stream_len//2)-1)])/2
            return res

        
        else:
            
            return self.stream[(self.stream_len//2)]



        