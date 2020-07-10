class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_to_int = 0

        # find where to add
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:      # if needs to round up
                digits[i] = 0
                if i == 0:          # if needs to round up and add more digit
                    digits.insert(0, 1)
                    break
                continue
            else:       # if normal case, just add one
                digits[i] += 1
                break

        return digits
