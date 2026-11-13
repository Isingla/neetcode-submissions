class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2

        total_len = len(A) + len(B)

        pile_size = (total_len + 1) // 2

        l, r = 0, len(A) 

        while l <= r:
            take_a = l + (r - l) // 2
            take_b = pile_size - take_a

            if take_a >= 1:
                last_a = A[take_a - 1]
            else:
                last_a = float('-inf')

            if take_a <= len(A) - 1:
                left_a = A[take_a]
            else:
                left_a = float('inf')

            if take_b >= 1:
                last_b = B[take_b - 1]
            else:
                last_b = float('-inf')

            if take_b <= len(B) - 1:
                left_b = B[take_b]
            else:
                left_b = float('inf')
            
            if last_b > left_a:
                l = take_a + 1
            elif last_a > left_b:
                r = take_a - 1
            else:
                if total_len % 2 == 1:
                    return max(last_a, last_b)
                else:
                    return (max(last_a, last_b) + min(left_a, left_b)) / 2
