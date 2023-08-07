#Problem Statement
class Solution:
    def twoSum(self, List, target):
        l = len(List)
        for i in range(0,l-1):
            for j in range(i+1,l):
                if List[i]+List[j]==target:
                    return([i,j])
Solution.twoSum([1,2,3,4],5)