class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        

# PERFORMANCE
# Runtime 40 ms (Beats 40.12% of users with Python)
# Memory 12.62 MB (Beats 88.40% of users with Python)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = list(t)

        for s_ in s:
            if s_ not in t:
                return False
            else:
                t.remove(s_)

        if len(t) != 0:
            return False
        else:
            return True


# PERFORMANCE
# Runtime 952 ms (Beats 25.29% of users with Python)
# Memory 12.41 MB (Beats 88.85%% of users with Python)

# PERFECT SOLUTION   
# class Solution(object):
#     def isAnagram(self, s, t):
        
#         counter = dict(int)
        
#         for s_ in s:
#             counter[s_] += 1
            
#         for t_ in t:
#             counter[t_] -= 1
            
#         for c in counter:
#             if c != 0:
#                 return False
#         return True
        

if __name__ == '__main__':
    
    assert True == Solution().isAnagram(s="anagram", t ="nagaram")
    assert False == Solution().isAnagram(s="rat", t ="car")
    assert False == Solution().isAnagram(s="ab", t ="a")
