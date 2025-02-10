# Sequence Analysis Project

This project contains Python implementations for sequence analysis, including timing and complexity visualization.

## Requirements

The following Python packages are required:

| Package    | Version |
|------------|---------|
| numpy      | 1.24.0  |
| matplotlib | 3.7.1   |
| scipy      | 1.11.3  |

You can install these packages using pip:

```bash
pip install numpy matplotlib scipy
```

## Project Structure

The project contains the following files:
- `sequence.py`: Implementation and analysis of the sequence S_n = 3*S_(n-1) - S_(n-2)

## Running the Programs

### Sequence Analysis
To run the sequence analysis:

```bash
python sequence.py
```

This will:
1. Calculate the sequence values up to n=100,000
2. Generate timing analysis plots showing:
   - Linear fit analysis
   - Quadratic fit analysis
   - Cubic fit analysis
3. Display the plots and print the final sequence value

## Expected Output
- Three subplot figures showing different complexity fits
- Console output showing S_100000 value
- Execution time analysis through visual plots

## Notes
- The program may take several minutes to run due to large number calculations
- Memory usage is optimized using constant space complexity
- Actual runtime complexity shows super-linear (quadratic or cubic fit) growth due to large number operations.

### Sequence Calculator
The program implements a sequence defined by:
- S_n = 3*S_(n-1) - S_(n-2)
- Initial conditions: S_0 = 0, S_1 = 1

### Complexity Analysis
While the algorithm's structure suggests O(n) complexity, empirical results show super-linear growth due to:
- Growing size of sequence numbers
- System overhead for large number operations
- Memory management requirements

## Author
- Chris