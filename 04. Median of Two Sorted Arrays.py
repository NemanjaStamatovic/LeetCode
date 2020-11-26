class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size_1 = len(nums1) 
        size_2 = len(nums2) 
  
        res = [] 
        i, j = 0, 0
  
        while i < size_1 and j < size_2: 
            if nums1[i] < nums2[j]: 
                res.append(nums1[i]) 
                i += 1
  
            else: 
                res.append(nums2[j]) 
                j += 1
  
        res = res + nums1[i:] + nums2[j:]
    
        if len(res) % 2 == 1:
            return res[len(res)//2]
        else:
            return (res[len(res)//2 - 1] + res[len(res)//2]) / 2