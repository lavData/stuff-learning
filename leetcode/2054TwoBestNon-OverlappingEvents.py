import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sorted_events = sorted(events, key=lambda x: (x[0], x[1]))
        n = len(sorted_events)

        dp = [[0, 0]] * (len(sorted_events) + 1)

        start_times = [sorted_events[i][0] for i in range(n)]

        for i in range(n - 1, -1, -1):
            next_index = bisect.bisect_right(start_times, sorted_events[i][1])
            next_index_next = (
                bisect.bisect_right(start_times, sorted_events[next_index][1])
                if next_index < n
                else n + 1
            ) - 1

            if sorted_events[i] == [67, 76, 81]:
                print(next_index, next_index_next)
                print(dp[next_index : next_index_next + 1])
                print(
                    max(
                        dp[next_index : next_index_next + 1],
                        key=lambda x: max(x) + sorted_events[i][2],
                    )
                )
            next_value = sorted(
                [sorted_events[i][2]]
                + max(
                    dp[next_index : next_index_next + 1],
                    key=lambda x: max(x) + sorted_events[i][2],
                ),
            )[-2:]

            dp[i] = max(dp[i + 1], next_value, key=lambda x: x[0] + x[1])

        print(dp)
        return dp[0][0] + dp[0][1]


if __name__ == "__main__":

    events = [
        [1, 86, 41],
        [2, 56, 74],
        [3, 31, 21],
        [4, 26, 22],
        [6, 94, 73],
        [11, 68, 72],
        [11, 99, 66],
        [13, 93, 49],
        [14, 71, 33],
        [14, 78, 37],
        [16, 63, 86],
        [19, 89, 9],
        [20, 88, 78],
        [26, 98, 63],
        [28, 71, 92],
        [40, 73, 85],
        [42, 50, 93],
        [44, 69, 35],
        [49, 63, 11],
        [51, 82, 55],
        [51, 98, 88],
        [53, 76, 91],
        [56, 72, 72],
        [57, 82, 36],
        [59, 88, 93],
        [61, 82, 45],
        [65, 65, 40],
        [66, 78, 14],
        [67, 76, 81],
        [72, 95, 8],
        [74, 76, 11],
        [76, 82, 54],
        [77, 82, 66],
        [81, 91, 100],
        [84, 95, 86],
        [94, 96, 23],
        [94, 98, 42],
        [95, 97, 19],
        [96, 98, 38],
        [97, 100, 11],
        [100, 100, 50],
    ]

    print(Solution().maxTwoEvents(events))
