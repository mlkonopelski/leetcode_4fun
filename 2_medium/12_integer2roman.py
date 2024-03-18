class Solution:
    def intToRoman(self, num: int) -> str:

        ROMANS = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'             
        }

        ROMANS_SPECIAL = {
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }

        DECIMAL = {
            0: 1,
            1: 10,
            2: 100,
            3: 1000
        }

        roman = ''   

        for i, n in enumerate(str(num)[::-1]):
            n = int(n)
            decimal_order = DECIMAL[i]
            if n ==4 or n ==9:
                roman = ROMANS_SPECIAL[n*decimal_order] + roman
                continue

            if n >= 5:
                mult_5 = ROMANS[5 * decimal_order]
                n = n - 5
                roman = mult_5 + n * ROMANS[decimal_order] + roman

            else:
                roman = n * ROMANS[decimal_order] + roman

        return roman


# PERFORMANCE
# Runtime 51 ms (Beats 35.98% of users with Python)
# Memory 16.61 MB (Beats 28.65% of users with Python)


if __name__ == '__main__':

    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"
