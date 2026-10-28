class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        curr_bills={5:0,10:0,20:0}

        for i in range( len(bills)):
            if bills[i]==5:
                curr_bills[5]+=1
            elif bills[i]==10:
                if curr_bills[5]>0:
                    curr_bills[5]-=1
                    curr_bills[10]+=1

                else:
                    #print("OOF")
                    return False
            elif bills[i]==20:
                if  curr_bills[10]>0 and curr_bills[5]>0:
                    curr_bills[10]-=1
                    curr_bills[5]-=1
                elif curr_bills[5]>=3:
                    curr_bills[5]=curr_bills[5]-3
                else:
                   # print("ROUGH")
                    return False
        return True
