class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in visited:
                return [visited[remaining], i]
            visited[v] = i
        return []