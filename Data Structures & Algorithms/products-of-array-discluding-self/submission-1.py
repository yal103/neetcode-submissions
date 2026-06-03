class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [1] * n
        after = [1] * n
        result = [1] * n
        
        for i in range(1, n):
            before[i] = nums[i - 1] * before[i - 1]
        for i in range(n - 2, -1, -1):
            after[i] = nums[i + 1] * after[i + 1]
        for i in range(n):
            result[i] = before[i] * after[i]
        return result

                