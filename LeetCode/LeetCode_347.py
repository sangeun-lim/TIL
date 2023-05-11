class Solution:
    # Counter를 이용한 음수 순 추출
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = []
        # k번 만큼 추출, 최소힙이므로 가장 작은 음수 순으로 추출

        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

#------------------------------------------------------------------#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]