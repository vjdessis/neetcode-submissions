class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):

            num = nums[i]
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i]
            
            else:
                seen[num] = i
