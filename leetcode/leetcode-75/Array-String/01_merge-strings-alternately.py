# url : https://leetcode.com/problems/merge-strings-alternately/

from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge strings by adding letters in alternating order.
        
        >>> solution = Solution()
        
        # Test case 1
        >>> solution.mergeAlternately("abc", "pqr")
        'apbqcr'
        
        # Test case 2  
        >>> solution.mergeAlternately("ab", "pqrs")
        'apbqrs'
        
        # Test case 3
        >>> solution.mergeAlternately("abcd", "pq")
        'apbqcd'
        """
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
