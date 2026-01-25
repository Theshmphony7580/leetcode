class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        for a, b in zip(s, s[1:]):  # Iterate through pairs (s[i], s[i+1])
            if roman[a] < roman[b]:  # If left value is smaller, subtract
                res -= roman[a]
            else:  # Otherwise, add the value
                res += roman[a]

        return res + roman[s[-1]]  # Add the last Roman numeral's value
