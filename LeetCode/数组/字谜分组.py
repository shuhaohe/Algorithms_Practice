class Solution:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for i in range(len(strs)):
            dic[str(sorted(strs[i]))].append(strs[i])
        return [i for i in dic.values()]