class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            char_counts = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                char_counts[index] += 1
            key = tuple(char_counts)
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)
        result = []
        for group in anagram_map.values():
            result.append(group)
        return result
        