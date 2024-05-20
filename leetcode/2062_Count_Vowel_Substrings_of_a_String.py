class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0

        stack_vowel = ["u", "o", "i", "e", "a"]
        for index, i in enumerate(word):
            if i in "aeiou":
                for j in word[index:]:
                    if j in "aeiou" and j in stack_vowel:
                        stack_vowel.remove(j)
                    elif j not in "aeiou":
                        break
                    if not stack_vowel:
                        count += 1
            stack_vowel = ["u", "o", "i", "e", "a"]

        return count


class Solution2:
    def countVowelSubstrings(self, word: str) -> int:
        maps = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        # k and i are two pointers in typical same direction sliding window problem, j is used to mark start point
        j, k, vow, res = 0, 0, 0, 0
        for i in range(len(word)):
            print(word[i])
            if word[i] in maps:
                maps[word[i]] += 1
                if maps[word[i]] == 1:
                    vow += 1
                while vow == 5:
                    maps[word[k]] -= 1
                    if maps[word[k]] == 0:
                        vow -= 1
                    k += 1
                res += k - j
                print("maps", maps)
                print("result", res)
            else:
                # reset pointers and maps
                maps = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
                vow = 0
                j, k = i + 1, i + 1
        return res


if __name__ == "__main__":
    print(Solution2().countVowelSubstrings("uaieuoua"))
