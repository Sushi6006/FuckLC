# 06/17/2020 22:36

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        res = []
        for i, person in enumerate(groupSizes):
            satisfied = False
            for group in res:
                req_size = groupSizes[group[0]]
                if len(group) < req_size and req_size == person:
                    group.append(i)
                    satisfied = True
            if not satisfied:
                res.append([i])
        
        return res