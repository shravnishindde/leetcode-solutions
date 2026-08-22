class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a = []
        for i in range(left, right + 1):
            s = str(i)
            # Check if '0' is not in the number and every digit divides i
            if '0' not in s and all(i % int(digit) == 0 for digit in s):
                a.append(i)
        return a

        