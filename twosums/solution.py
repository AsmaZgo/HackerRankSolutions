class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind_i=0
        
        for i in nums:
            ind_j=0
            for j in nums:
                if (ind_i <> ind_j) and (i+j == target):
                    return [ind_i, ind_j]
                ind_j=ind_j+1
            
            ind_i=ind_i+1
        return []
