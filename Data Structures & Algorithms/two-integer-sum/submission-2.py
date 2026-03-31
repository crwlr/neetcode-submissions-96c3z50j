class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lost_and_found = dict()

        for i, num in enumerate(nums):
          complement = target - num
          if complement in lost_and_found:
            return [lost_and_found[complement], i]
          else:
            lost_and_found[num] = i

        return []
