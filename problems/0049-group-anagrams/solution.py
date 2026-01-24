from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_key = "".join(sorted(word))

            anagram_map[sorted_key].append(word)
        return list(anagram_map.values())


        # final = list()
        # for word in strs:
        #     sorted_ = "".join(sorted(word))
        #     sorted_dict = {}
        #     # for same in sorted_:
        #     #     print(same)
            
        #     final.append(sorted_)
        # for word2 in final:
        #     if word
        #     print(word2)
        # # print(final)
        
