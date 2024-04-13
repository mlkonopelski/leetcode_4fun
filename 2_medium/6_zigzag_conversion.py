class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        s = list(s)

        # CREATE EMPTY TABLE TO POPULATE
        col_input = True
        cols = 1
        diag = 0
        for i in range(1, len(s)):
            if col_input:
                if i % numRows == 0:
                    cols += 1
                    col_input = False
            else:
                if diag == numRows - 2:
                    col_input = True
                    diag = 0
                    cols += 1
                    continue 
                cols += 1
                diag +=1

        table = [['' for _ in range(cols)] for _ in range(numRows)]


        # POPULATE THIS TABLE
        col_input = True # if diagonal false
        col = 0
        while s:
            if col_input:
                for i in range(min(numRows, len(s))):
                    table[i][col] = s.pop(0)
                col += 1
                col_input = False
            else:
                for i in range(min(numRows-2, len(s))):
                    table[numRows-i-1-1][col] = s.pop(0)
                    col += 1
                col_input = True

        # RETURN STRING FROM ROWS
        r_s = ''.join([''.join(row) for row in table])
        
        return r_s


# PERFORMANCE
# Runtime 202 ms (Beats 8.92% of users with Python)
# Memory 18.90 MB (Beats 7.45% of users with Python)


if __name__ == '__main__':

    assert Solution().convert("PAYPALISHIRING", numRows = 3) == 'PAHNAPLSIIGYIR'
    assert Solution().convert("PAYPALISHIRING", numRows = 4) == 'PINALSIGYAHRPI'
    assert Solution().convert("PAYPALISHIRING", numRows = 7) == 'PNAIGYRPIAHLSI'
    assert Solution().convert(s = "A", numRows = 1) == 'A'
