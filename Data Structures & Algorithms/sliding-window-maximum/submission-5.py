class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        mList = deque()

        for r in range(len(nums)):
            while mList and nums[r] > nums[mList[-1]]:
                mList.pop()

            mList.append(r)

            while r - l + 1 >= k:
                if mList[0] < l:
                    mList.popleft()
                res.append(nums[mList[0]])
                l += 1
            
        return res
        