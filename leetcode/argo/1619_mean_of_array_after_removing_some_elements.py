import random
from typing import List


class Solution:
    def quickselect(self, arr: List[int], k: int) -> int:
        if len(arr) == 1:
            return arr[0]

        pivot = random.choice(arr)

        lows = [el for el in arr if el < pivot]
        highs = [el for el in arr if el > pivot]
        pivots = [el for el in arr if el == pivot]

        if k < len(lows):
            return self.quickselect(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return self.quickselect(highs, k - len(lows) - len(pivots))

    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = int(n * 0.05)

        lower_bound = self.quickselect(arr, k)
        upper_bound = self.quickselect(arr, n - k - 1)

        trimmed_elements = [x for x in arr if lower_bound <= x <= upper_bound]

        trimmed_mean = sum(trimmed_elements) / len(trimmed_elements)

        return trimmed_mean


# Test the Solution class
solution = Solution()

# Test cases
arr1 = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 8, 9, 10, 11, 12, 13, 14]
arr2 = [6, 2, 7, 5, 1, 2, 0, 9, 8, 4]
arr3 = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 1, 6, 6, 3, 8, 4, 2, 0, 8, 8]

# Results
print(
    solution.trimMean(arr1)
)  # Expected to be around the mean of central elements after removing 5% from both ends
print(
    solution.trimMean(arr2)
)  # Expected to be around the mean of central elements after removing 5% from both ends
print(
    solution.trimMean(arr3)
)  # Expected to be around the mean of central elements after removing 5% from both ends
