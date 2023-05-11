class Solution:
    # 해시 테이블을 이용한 풀이
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        cnt = 0

        # 돌의 빈도수 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # 보석의 빈도수 합산
        for char in jewels:
            if char in freqs:
                cnt += freqs[char]

        return cnt

#---------------------------------------------------------------#
class Solution:
    # Counter로 계산 생략
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)  # 돌 빈도수 계산
        cnt = 0

        # 비교 없이 보석 빈도수 합산
        for char in jewels:
            cnt += freqs[char]

        return cnt

#---------------------------------------------------------------#
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
