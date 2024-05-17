import time

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        results = []
        
        if len(digits) == 0:
            return []
        else:
            results = mapping[digits[0]]
            digits = digits[1:]
        for d in digits:
            temp = []
            for word in results:
                for entry in mapping[d]:
                    temp.append(word + entry)
            results = temp
        return results
    
    def test(self, digits: str) -> list[str]:
        return self.letterCombinations(digits)

def main():
    print(Solution().test("23456789"))

if __name__ == "__main__":
    main()