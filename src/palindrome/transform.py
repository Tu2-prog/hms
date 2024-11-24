import math


class Transform:
    def reverse_number(self, num: int) -> int:
        """
        The reverse_number method takes an int and reverses it using a recursive approach
        :param num: The number to be reversed
        :return: Int n that was reversed
        """
        return int(num != 0) and (
            (num % 10) * (10 ** int(math.log(num, 10))) + self.reverse_number(num // 10)
        )

    def palindrome(self, n: int) -> (int, int):
        """
        The palindrome method takes an int n and either returns n when n is already a palindrome or it
        transforms n into a palindrome, but if the number cannot be transformed into palindrome, the special
        value -1 gets returned.
        :param n: The number that is needed to be transformed into a palindrome
        :return: Int n that is either the (transformed) number which is a palindrome or -1 if a transformation is
        infeasible
        """
        cycle_count = 0

        if self.is_palindrome(n):
            return n, cycle_count

        while n <= 1000000000:
            n += self.reverse_number(n)
            cycle_count += 1
            if self.is_palindrome(n):
                return n, cycle_count

        return -1, cycle_count

    def is_palindrome(self, n) -> bool:
        """
        The is_palindrome method checks whether a given number is a palindrome or not.
        :param n: The number n to check
        :return: Boolean stating if the reverse of the number is a palindrome or not
        """
        return n == self.reverse_number(n)
