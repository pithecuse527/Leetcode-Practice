class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_to_int = 0

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    break
                continue
            else:
                digits[i] += 1
                break

        return digits
