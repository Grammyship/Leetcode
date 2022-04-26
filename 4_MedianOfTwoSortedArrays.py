class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        m = len(nums1)
        n = len(nums2)
        count = (m+n)/2

        # merge two List
        nums = []
        Lptr = 0
        Rptr = 0
        while ((Lptr<m)or(Rptr<n)):
            if Rptr == n:
                nums.append(nums1[Lptr])
                Lptr += 1
            elif Lptr != m and nums1[Lptr] < nums2[Rptr]:
                nums.append(nums1[Lptr])
                Lptr += 1
            else:
                nums.append(nums2[Rptr])
                Rptr += 1
                
        return nums[count] if (m+n)%2==1 else (float(nums[count])+float(nums[count-1]))/2
        
                
            
