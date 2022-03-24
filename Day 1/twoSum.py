class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[];
        for i in range(0,len(nums)):
            print(i)
            diff=target-nums[i]
            print(diff)
            number=0
            for j in range(0,len(nums)):
                if(nums[j]==diff and nums[j]!=i):
                    number=j
                    break
            if(number!=0):
                arr.append(i)
                arr.append(j)
                break
        return(arr)