class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i, s in enumerate(strs):
          key = "".join(sorted(s))

          if key in groups:
              groups[key].append(s)
          else:
              groups[key] = [s]

        return list(groups.values())

    
