# There is a dungeon with n x m rooms arranged as a grid.
#
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
#
# Return the minimum time to reach the room (n - 1, m - 1).
#
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.
#
#
#
# Example 1:
#
# Input: moveTime = [[0,4],[4,4]]
#
# Output: 6
#
# Explanation:
#
# The minimum time required is 6 seconds.
#
# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in one second.
#
# Example 2:
#
# Input: moveTime = [[0,0,0],[0,0,0]]
#
# Output: 3
#
# Explanation:
#
# The minimum time required is 3 seconds.
#
# At time t == 0, move from room (0, 0) to room (1, 0) in one second.
# At time t == 1, move from room (1, 0) to room (1, 1) in one second.
# At time t == 2, move from room (1, 1) to room (1, 2) in one second.
#
# Example 3:
#
# Input: moveTime = [[0,1],[1,2]]
#
# Output: 3
#
#
#
# Constraints:
#
# 2 <= n == moveTime.length <= 50
# 2 <= m == moveTime[i].length <= 50
# 0 <= moveTime[i][j] <= 109
#
import heapq
from collections import deque
from typing import List


# dijkstra
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        pq = [(0, 0, 0)]
        visited = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

        while pq:
            time, x, y = heapq.heappop(pq)

            if (x, y) == (n-1, m-1):
                return time

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    next_time = max(time, moveTime[nx][ny]) + 1

                    if (nx, ny) not in visited:
                        heapq.heappush(pq, (next_time, nx, ny))

        return -1


class Solution2:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        dp = [[float('inf')] * m for _ in range(n)]
        dp[0][0] = 0

        queue = deque([(0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            i, j = queue.popleft()
            current_time = dp[i][j]

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < m:
                    departure_time = max(current_time, moveTime[ni][nj])
                    arrival_time = departure_time + 1

                    if arrival_time < dp[ni][nj]:
                        dp[ni][nj] = arrival_time
                        queue.append((ni, nj))

        return dp[-1][-1]



def test_case():
    assert Solution().minTimeToReach([[0, 4], [4, 4]]) == 6
    assert Solution2().minTimeToReach([[0, 4], [4, 4]]) == 6


if __name__ == '__main__':
    test_case()