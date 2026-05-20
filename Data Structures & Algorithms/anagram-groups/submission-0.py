class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_map = defaultdict(list)
        for s in strs:
            sign = tuple(sorted(s))
            anag_map[sign].append(s)

        return list(anag_map.values())

        