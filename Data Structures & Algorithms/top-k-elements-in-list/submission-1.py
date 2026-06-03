class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        # make a list where index corresponds with number of occurrences
        # at most len(nums) + 1 occurrences
        result = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        for num, cnt in counter.items():
            result[cnt].append(num)
        
        # remove the empty arrays, take last k elements
        result = [arr for arr in result if arr][-k:]
        final = []
        for arr in result:
            for num in arr:
                final.append(num)
        return final[-k:]
