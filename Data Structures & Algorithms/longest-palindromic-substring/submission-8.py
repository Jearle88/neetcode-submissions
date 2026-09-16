class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n=len(s)

        if n==1:
            return s
        res=""
        res_len=1
        left_idx=0
        right_idx=0
        for i in range(n):
            left=i
            right=i

            while left>=0 and right<n and s[right]==s[left]:
                if (right-left)>res_len:
                    right_idx=right
                    left_idx=left
                    res_len=right-left
                right+=1
                left-=1
            
            #even substrign case
            left=i
            right=i+1
            
            while left>=0 and right<n and s[right]==s[left]:
                if (right-left+1)>res_len:
                    right_idx=right
                    left_idx=left
                    res_len=right-left
                right+=1
                left-=1
       # print("left",left_idx)
        #print("right",right_idx)
        return s[left_idx:right_idx+1]