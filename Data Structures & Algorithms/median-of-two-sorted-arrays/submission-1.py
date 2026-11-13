class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        l,r=0,len(nums1)-1
        half = total//2
        while True:
            i = l+(r-l)//2
            j = half-i-2

            Aright = nums1[i+1] if (i+1) < len(nums1) else math.inf
            Aleft = nums1[i] if i >=0 else -math.inf
            Bright = nums2[j+1] if (j+1)< len(nums2) else math.inf
            Bleft=nums2[j] if j>=0 else -math.inf

            if Aleft <= Bright and Bleft <=Aright:
                if total%2:
                    return min(Aright,Bright)
                else:
                    return (max(Bleft,Aleft)+min(Bright,Aright))/2
            else:
                if Aleft > Bright:
                    r=i-1
                else:
                    l+=1