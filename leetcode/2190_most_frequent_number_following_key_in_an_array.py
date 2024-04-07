class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count_dict = {}

        index = 1
        while index < len(nums):
            if nums[index - 1] == key:
                count = 1

                current_value = nums[index]
                j = index + 1

                while j < len(nums) and nums[j] == current_value:
                    count += 1
                    j += 1

                count_dict[current_value] = max (count_dict.get(current_value, 0), count)

                index = j
            else:
                index += 1
        
        return max(count_dict, key = count_dict.get)



// Other Solution 

class Solution2:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        start_index = 1
        while start_index < len(nums) or nums[start_index] != key:
	        start_index += 1
        return max_frequent(nums[start_index:])

    def max_frequent(self, nums):
	    return max(set(nums), key = lamda x: nums.count(x))
