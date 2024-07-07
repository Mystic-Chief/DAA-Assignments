"""
33. Solve the Towers of Hanoi problem
"""

class Solution(object):
    def towersOfHanoi(self, n, source, auxiliary, target):
        """
        :type n: int
        :type source: str
        :type auxiliary: str
        :type target: str
        :rtype: None
        """
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        self.towersOfHanoi(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        self.towersOfHanoi(n - 1, auxiliary, source, target)


