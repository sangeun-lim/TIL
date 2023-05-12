class Solution:
    # DFS로 k개 조합 생성
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return results

#---------------------------------------------------------#
class Solution:
    # itertools 모듈 사용
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))