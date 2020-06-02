class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left=maxVal=0
        dist=right=len(height)-1
        
        while left < right:
            curVal = dist * min(height[left],height[right])
            if maxVal < curVal:
                maxVal = curVal
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            dist-=1
            
        return maxVal
