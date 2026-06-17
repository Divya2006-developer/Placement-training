class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length


if __name__ == "__main__":

    sol = Solution()
    
    print("--- Longest Substring Without Repeating Characters ---")
    print("Instructions: Type or paste your string below and press Enter.")
    print("Examples to try: 'abcabcbb', 'bbbbb', 'pwwkew'\n")
    

    user_input = input("Enter your string: ")

    result_length = sol.lengthOfLongestSubstring(user_input)
    

    print(f"Output: {result_length}")
