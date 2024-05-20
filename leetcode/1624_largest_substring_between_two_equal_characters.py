class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_character = {}
        max_largest = -1

        for index, i in enumerate(s):
            if i in first_character:
                current_length = index - first_character[i] - 1
                max_largest = max(max_largest, current_length)
            else:
                first_character[i] = index

        return max_largest


if __name__ == "__main__":
    s = "aa"
    print(Solution().maxLengthBetweenEqualCharacters(s))  # Expected 0

    s = "abca"
    print(Solution().maxLengthBetweenEqualCharacters(s))  # Expected 2

    s = "cbzxy"
    print(Solution().maxLengthBetweenEqualCharacters(s))  # Expected -1)

    s = "mgntdygtxrvxjnwksqhxuxtrv"
    print(Solution().maxLengthBetweenEqualCharacters(s))  # Expected 18
