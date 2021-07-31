"""
4. Median of Two Sorted Arrays
Time Submitted: 07/26/2021 12:21
"""


class Solution(object):
    def findmid(self, nums1, nums2, mid):
        m = len(nums1)
        n = len(nums2)
        if n < m:
            return self.findmid(nums2, nums1, mid)
        if m == 0:
            return nums2[mid-1]
        if mid == 1:
            return min(nums1[0], nums2[0])

        # if m > mid/2, check = pos
        check = min(mid/2, m)
        pos = mid-check

        if nums1[check-1] <= nums2[pos-1]:
            """
            if nums1 is smaller, we can delete all of it
            nums1[check:] = []
            """
            return self.findmid(nums1[check:], nums2, pos)
        else:
            """
            delete nums2[0:pos]
            """
            return self.findmid(nums1, nums2[pos:], check)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m+n) % 2 == 1:
            return self.findmid(nums1, nums2, (m+n)/2+1)
        else:
            return (self.findmid(nums1, nums2, (m+n)/2) + self.findmid(nums1, nums2, (m+n)/2+1)) / 2.0
