class Solution:
    # 짝수 번째 값 계산
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                total += n

        return total