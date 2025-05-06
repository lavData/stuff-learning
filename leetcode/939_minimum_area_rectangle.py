# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].
#
# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0

from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # retangle require at least 4 point that (r1, c1) (r1, c2) (r2, c1) (r2, c2)

        point_set = set(map(tuple, points))

        min_area = float('inf')

        n = len(points)


        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0


# test case
def test_case():
    assert Solution().minAreaRect([[1,3],[3,3],[1,4],[3,4]]) == 2


if __name__ == "__main__":
    test_case()
