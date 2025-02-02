class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        #current number variables
        #n1 is used as a current number variable, n2 is used as a last number variable.
        #n2 is only used if the combined length of the arrays is even.
        n1 = 0
        n2 = 0
        #pointer variables
        #i points to the latest index for nums1, j to the latest index for nums2
        i = 0
        j = 0
        #array length variables
        len1 = len(nums1)
        len2 = len(nums2)

        #In this implementation I'm iterating through half of the array to find the median.
        #I'm not merging and re-sorting the two arrays, so I have to find a way to treat them as 1 array.
        #Operationally, I'm comparing the lowest value between the two arrays and incrementing the pointer of the lowest one, functionally dropping it from its array.
        
        for count in range((len1 + len2)/2+1):
            #set last number equal to last number
            n2=n1
            #check if specific operations need to occur to avoid an out of bounds exception.
            if i < len1 and j < len2:
                #check current numbers.
                if nums1[i] < nums2[j]:
                    #if nums1 number is lower, increment i and update n1
                    n1 = nums1[i]
                    i+=1
                else:
                    #if nums2 number is lower, increment j and update n1
                    n1 = nums2[j]
                    j+=1
            #if an out of bounds operation might occur, it means that the array is empty. 
            #In this scenario, the other array gets incremented.
            elif i == len1:
                n1 = nums2[j]
                j+=1
            else:
                n1 = nums1[i]
                i+=1
            
        #Determine if the combined length of the arrays is even or odd, then find the median.
        if (len1 + len2) % 2 == 1:
            return n1
        else:
            ans = float(n1+n2)
            return ans/2
