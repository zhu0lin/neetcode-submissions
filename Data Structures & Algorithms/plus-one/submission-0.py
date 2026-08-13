class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Understand
        Input: An integer array digits, where each digits[i] is
        the ith digit of an integer.
        Output: The integer array of this integer incrmeneted by one.

        Plan:
        We can probably start iterating at the end of the digits array
        We add 1 to digits[-1] and if 1+digits[-1] < 10, we can
        update digits[-1] and return the array

        At ANY point, when 1+digits[i] < 10, we can update digits[i]
        and return the array

        Otherwise if 1+digits[-1] >= 10, we need to do carries onto
        the lhs integers. Let sum = 1+digits[-1] and update
        digits[-1] to be sum % 10. Let the carry be sum // 10.

        [1, 8, 9]
        [1, 9, 0]
        """
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                sum_at_digit = 1 + digits[i] 
            else:
                sum_at_digit = digits[i] + carry
            
            if sum_at_digit < 10:
                digits[i] = sum_at_digit
                return digits
            else:
                digits[i] = sum_at_digit % 10
                carry = sum_at_digit // 10

        if carry:
            digits.insert(0, carry)
        return digits