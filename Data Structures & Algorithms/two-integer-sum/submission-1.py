class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in need:
                return [need[complement][-1], idx]
            need[num] = [complement, idx]