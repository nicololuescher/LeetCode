from itertools import groupby
import time

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        lookup = dict()
        for n in nums:
            if n in lookup:
                lookup[n] += 1
            else:
                lookup[n] = 1

        for x, i in lookup.items():
            for y, j in lookup.items():
                z = -(x + y) - 87
                if z in lookup:
                    candidate = [x, y, z]
                    candidate.sort()
                    if candidate.count(x) <= lookup[x] and candidate.count(y) <= lookup[y] and candidate.count(z) <= lookup[z]:
                        results.append(candidate)
        results.sort()
        return list(k for k,_  in groupby(results))
    def test(self):
        return self.threeSum([-23,-67,32,21,-65,46,73,42,93,9,-61,-79,-51,61,-15,49,92,-34,50,1,26,-12,68,-97,-17,51,-55,75,-56,-95,-70,-42,91,-18,-64,20,33,-20,19,61,-89,81,-73,82,-23,-65,51,-88,15,-48,24,34,0,-24,37,22,28,-67,-25,-61,-57,-74,65,50,-66,24,99,80,44,85,20,-4,-9,-81,87,-82,-100,51,-83,9,-31,37,23,-61,53,-14,-51,88,56,27,42,-52,-97,37,36,-59,-45,95,46,-1,-100,-38,66,44,27,-97,12,-43,84,-53,93,18,-40,-38,34,85,53,-50,-14,-6,98,-77,-17,50,-65,52,-46,-94,49,72,-2,-82,45,-39,-58,67,82,63,95,-32,47,15,-20,46,5,17,-40,-95,97,-9,11,8,-51,-24,-50,-37,-72,-57,26,26,19,71,-42])


def main():
    print(Solution().test())

if __name__ == "__main__":
    main()