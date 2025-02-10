# (1)
# Complete the sequence_calculator function, which should
# Return the n-th number of the sequence S_n, defined as:
# S_n = 3*S_(n-1) - S_(n-2), with S_0 = 0 and S_1 = 1.
# Your implementation should minimize the execution time.
#
# (2)
# Find the time complexity of the proposed solution, using
# the "Big O" notation, and explain in detail why such
# complexity is obtained, for n ranging from 0 to at least
# 100000. HINT: you are dealing with very large numbers!
#
# (3)
# Plot the execution time VS n (again, for n ranging from 0
# to at least 100000).
#
# (4)
# Confirm that the empirically obtained time complexity curve
# from (3) matches the claimed time complexity from (2) (e.g.
# by using curve fitting techniques).
#

import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import curve_fit

def sequence_calculator(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Use dynamic programming with only two variables to minimize memory usage
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1): # O(n)
        current = 3 * prev1 - prev2 # O(1)
        prev2, prev1 = prev1, current # O(1)
    
    return prev1

def measure_execution_time(n): 
    start_time = time.time()
    result = sequence_calculator(n)
    end_time = time.time()
    return end_time - start_time

def linear_fit(x, a, b):
    return a * x + b

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Generate data points for time complexity analysis
n_values = np.linspace(0, 100000, 50, dtype=int)
times = []

for n in n_values:
    execution_time = measure_execution_time(n)
    times.append(execution_time)

# Plot execution time vs n
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'b.', label='Measured times')
plt.xlabel('n')
plt.ylabel('Execution time (seconds)')
plt.title('Time Complexity Analysis')

# Curve fitting to confirm O(n) complexity
popt, _ = curve_fit(quadratic_fit, n_values, times)
plt.plot(n_values, quadratic_fit(n_values, *popt), 'r-', 
         label=f'Quadratic fit (ax^2 + bx + c)\na={popt[0]:.2e}, b={popt[1]:.2e}, c={popt[2]:.2e}') ## O(n^2) * a + O(n) * b + c

plt.legend()
plt.grid(True)
plt.show()

# Print result for n=100000
print(f"S_{100000} = {sequence_calculator(100000)}")
