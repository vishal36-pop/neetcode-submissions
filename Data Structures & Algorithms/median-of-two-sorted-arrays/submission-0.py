class Solution:
    def  findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        # Always binary search on the smaller array
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        left_size = (m + n + 1) // 2

        low, high = 0, m

        while low <= high:

            partA = (low + high) // 2
            partB = left_size - partA

            leftA = float("-inf") if partA == 0 else nums1[partA - 1]
            rightA = float("inf") if partA == m else nums1[partA]

            leftB = float("-inf") if partB == 0 else nums2[partB - 1]
            rightB = float("inf") if partB == n else nums2[partB]

            # Correct partition
            if leftA <= rightB and leftB <= rightA:

                if (m + n) % 2 == 1:
                    return max(leftA, leftB)

                return (max(leftA, leftB) + min(rightA, rightB)) / 2

            # Took too many elements from nums1
            elif leftA > rightB:
                high = partA - 1

            # Took too few elements from nums1
            else:
                low = partA + 1