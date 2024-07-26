"""
28. Page Faults in LRU
"""

class Solution(object):
    def pageFaults(self, pages, capacity):
        """
        :type pages: List[int]
        :type capacity: int
        :rtype: int
        """
        s = set()
        indexes = {}
        page_faults = 0
        
        for i in range(len(pages)):
            if len(s) < capacity:
                if pages[i] not in s:
                    s.add(pages[i])
                    page_faults += 1
            else:
                if pages[i] not in s:
                    lru = min(indexes, key=indexes.get)
                    s.remove(lru)
                    s.add(pages[i])
                    page_faults += 1
            indexes[pages[i]] = i
        
        return page_faults

