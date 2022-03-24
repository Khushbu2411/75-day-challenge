class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1;
        for i in range(len(digits),1,-1):
            if(digits[i-1]==10):
                digits[i-2]=digits[i-2]+1
                digits[i-1]=0
        if(digits[0]==10):
            digits[0]=0;
            digits.insert(0,1);
        
        return(digits)  