class Solution:
    def isPalindrome(self,num:int) -> bool:
        num = str(num)
        
        if num == num[::-1]:
            return True  # It is a palindrome
        else:
            return False
         
s = Solution()
print(s.isPalindrome(123))
