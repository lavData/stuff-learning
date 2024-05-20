import random
from typing import List


class Solution:
    def partition(self, arr, left, high):
        pivot = arr[high]
        i = left - 1

        for j in range(left, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def select_k_smallest(self, arr, left, high, k):
        if k > 0 and k <= high - left + 1:
            pivot = self.partition(arr, left, high)

            if pivot - left == k - 1:
                return

            if pivot - left > k - 1:
                return self.select_k_smallest(arr, left, pivot - 1, k)

            return self.select_k_smallest(arr, pivot + 1, high, k - (pivot - left + 1))

    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        num_trim = n // 20

        self.select_k_smallest(arr, 0, n - 1, num_trim)
        self.select_k_smallest(arr, num_trim, n - 1, n - num_trim)

        return sum(arr[num_trim : n - num_trim]) / (n - num_trim * 2)


# Test the Solution class
solution = Solution()

# Test case
arr = [
    15375,
    14402,
    78024,
    4091,
    90536,
    44860,
    91453,
    28153,
    98485,
    62993,
    76236,
    94820,
    76539,
    29613,
    55240,
    19368,
    50257,
    92655,
    45863,
    10728,
    76248,
    34825,
    61465,
    174,
    76856,
    9236,
    6345,
    74709,
    37307,
    98785,
    73200,
    37197,
    29381,
    97010,
    57100,
    37370,
    56396,
    59834,
    51721,
    30022,
    60736,
    72549,
    39983,
    54952,
    17863,
    85716,
    14665,
    96461,
    5379,
    24249,
    61660,
    83580,
    35930,
    8730,
    81722,
    1063,
    97338,
    26084,
    58923,
    80295,
    85955,
    59607,
    50939,
    42582,
    63999,
    30211,
    51976,
    38452,
    87311,
    63340,
    33449,
    96623,
    6981,
    59380,
    30121,
    96658,
    29946,
    82092,
    53459,
    76135,
    73926,
    96594,
    47171,
    14997,
    5340,
    94902,
    44871,
    49539,
    36986,
    64194,
    14675,
    33824,
    83597,
    36483,
    38419,
    8259,
    2226,
    79056,
    3263,
    62303,
    18869,
    69287,
    38342,
    67877,
    49266,
    85272,
    78396,
    88763,
    71572,
    36995,
    36379,
    46421,
    58566,
    67268,
    16266,
    45500,
    54815,
    58317,
    95662,
    78299,
]

print(solution.trimMean(arr))  # Should produce the correct trimmed mean
