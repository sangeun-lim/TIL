class Solution:
    # 스택 값 비교
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 ans 값 갱신
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                ans[last] = i - last
            stack.append(i)

        return ans