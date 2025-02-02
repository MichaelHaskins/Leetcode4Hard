class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        n1 = 0
        n2 = 0
        i = 0
        j = 0
        len1 = len(nums1)
        len2 = len(nums2)

        for count in range((len1 + len2)/2+1):
            n2=n1
            if i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    n1 = nums1[i]
                    i+=1
                else:
                    n1 = nums2[j]
                    j+=1
            elif i == len1:
                n1 = nums2[j]
                j+=1
            else:
                n1 = nums1[i]
                i+=1
            
        if (len1 + len2) % 2 == 1:
            return n1
        else:
            ans = float(n1+n2)
            return ans/2
