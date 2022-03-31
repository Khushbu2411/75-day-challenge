class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        n=len(nums)-1
        last=len(nums)-1
        first=0
        while(first<=last):
            if(nums[first]*nums[first]>nums[last]*nums[last]):
                arr[n]=(nums[first]*nums[first])
                first+=1
            else:
                arr[n]=(nums[last]*nums[last])    
                last-=1
            n-=1 
        return(arr)
            
                    
                    
        