"""
6. Maximum Units on a Truck
"""

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[Tuple[int, int]] # (number of boxes, units per box)
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        max_units = 0
        
        for boxes, units in boxTypes:
            if truckSize == 0:
                break
            if boxes <= truckSize:
                max_units += boxes * units
                truckSize -= boxes
            else:
                max_units += truckSize * units
                truckSize = 0
                
        return max_units

