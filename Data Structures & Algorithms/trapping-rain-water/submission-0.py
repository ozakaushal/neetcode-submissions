class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1        # l starts at the left end, r at the right end
        left_max = 0                      # tallest bar seen so far from the left
        right_max = 0                     # tallest bar seen so far from the right
        res = 0                           # total trapped water

        while left < right:                      # keep going until the pointers meet
            if height[left] < height[right]:     # left bar is shorter, so the left side decides the water
                if height[left] >= left_max:
                    left_max = height[left]  # new tallest wall on the left, no water here
                else:
                    res += left_max - height[left]  # water = wall height minus bar height
                left += 1                    # move left pointer inward
            else:                         # right bar is shorter or equal
                if height[right] >= right_max:
                    right_max = height[right] # new tallest wall on the right, no water here
                else:
                    res += right_max - height[right]  # water on this bar
                right -= 1                    # move right pointer inward

        return res 
        