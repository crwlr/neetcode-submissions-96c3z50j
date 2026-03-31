class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lost_and_found = dict()

        for i in range(0, len(nums)):
          complement = target - nums[i]
          if complement in lost_and_found:
            return [lost_and_found[complement], i]
          else:
            lost_and_found[nums[i]] = i

        return []
