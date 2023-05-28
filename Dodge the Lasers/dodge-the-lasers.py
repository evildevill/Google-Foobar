from decimal import Decimal, localcontext

def solution(s):
    n = Decimal(s)
    with localcontext() as ctx:
        ctx.prec = 102
        r = Decimal(2).sqrt()
        s = Decimal(2) + Decimal(2).sqrt()

        def solve(n):
            # Base case: when n is 0, the sum is also 0
            if n == 0:
                return 0

            # Calculate Brn (integer part of r*n) and Brns (integer part of Brn/s)
            Brn = int(r * n)
            Brns = int(Decimal(Brn) / s)

            # Recursive formula: sum = (Brn * (Brn + 1)) / 2 - solve(Brns) - Brns * (Brns + 1)
            return (Brn * (Brn + 1)) / 2 - solve(Brns) - Brns * (Brns + 1)

        # Convert the result to string and return
        return str(int(solve(n)))
