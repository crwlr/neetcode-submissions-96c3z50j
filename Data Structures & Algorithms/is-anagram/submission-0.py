class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = dict()

        if len(s) != len(t):
            return False

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

    ## if any value is not zero, 
    # then 
        for ch in t:
          if counts.get(ch):
            counts[ch] = counts[ch] - 1
        
        for count in counts.values():
          if count !=0:
            return False
        
        return True

           
             
             
             

          