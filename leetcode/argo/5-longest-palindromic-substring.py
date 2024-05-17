class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_length = 0
        start = 0

        for i in range(len(s)):
            # odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    start = left
                left -= 1
                right += 1

            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    start = left
                left -= 1
                right += 1

        return s[start : start + max_length]


if __name__ == "__main__":
    s = "babad"
    result = Solution().longestPalindrome(s)
    print(f"result = {result}")
