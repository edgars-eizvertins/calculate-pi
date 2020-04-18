#!/usr/bin/env python3

#   Use Machin's Formula
#   pi = 4*(4*arctan(1/5) - arctan(1/239))
#
import sys
import time

def CalculateArctan(d, digits_count):
    # Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
    total = term = (10**digits_count) // d
    n = 0
    while term != 0:
        n += 1
        term //= -d*d
        total += term // (2*n + 1)    
    return total

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('USAGE: pi.py digits_count file_name')
        sys.exit(1)

    start_time = time.time()

    extra_digits = 10             # Extra digits to reduce trailing error
    digits_count = int(sys.argv[1])

    # Use Machin's Formula to calculate pi.
    pi = 4 * (4*CalculateArctan(5,digits_count + extra_digits) - CalculateArctan(239,digits_count + extra_digits))
    pi //= 10**extra_digits

    execution_time = time.time() - start_time
    print("--- %s seconds ---" % (execution_time))

    fileName = sys.argv[2]
    with open(fileName, 'wt') as outfile:
        outfile.write("Digits count: " + str(digits_count) + '\n')
        outfile.write("Execution time in seconds: %s \n\n" % execution_time)

        text = str(pi)        
        outfile.write(text[0] + '.' + text[1:] + '\n')
    
    sys.exit(0)