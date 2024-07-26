"""
27. Minimum Platforms
"""

class Solution(object):
    def minPlatforms(self, arrivals, departures):
        """
        :type arrivals: List[int]
        :type departures: List[int]
        :rtype: int
        """
        arrivals.sort()
        departures.sort()
        i, j = 0, 0
        platforms_needed, max_platforms = 0, 0
        
        while i < len(arrivals) and j < len(departures):
            if arrivals[i] <= departures[j]:
                platforms_needed += 1
                max_platforms = max(max_platforms, platforms_needed)
                i += 1
            else:
                platforms_needed -= 1
                j += 1
        
        return max_platforms

