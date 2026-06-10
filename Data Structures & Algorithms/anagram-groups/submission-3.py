class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res: List[List[str]] = []

        mapList : List[dict] = []

        for string in strs:
            current_map= dict()
            for char in string:
                if char in current_map:
                    current_map[char] = current_map[char]+1
                else:
                    current_map[char] = 1
            exists = False
            for i,m in enumerate(mapList):
                if m == current_map:
                    res[i].append(string)
                    exists = True
            if not exists:
                new_list = []
                new_list.append(string)
                res.append(new_list)
                mapList.append(current_map)
                

        return res