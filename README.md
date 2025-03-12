# Quadratic Equation Solver

This application solves quadratic equations of the form:

```
ax^2 + bx + c = 0
```

It supports both interactive and non-interactive modes.

## How to Set Up Locally

1. Clone the repository:
   ```sh
   git clone https://github.com/meluni9/equation-solver.git
   cd equation-solver
   ```
2. Ensure you have Python installed (version 3.x recommended).

## How to Build and Run

### Running in Interactive Mode

Execute the script without arguments, and it will prompt you to enter the coefficients:

```sh
python main.py
```

Then, follow the on-screen instructions to input values for `a`, `b`, and `c`.

### Running in Non-Interactive Mode

Provide a text file containing three space-separated coefficients:

```sh
python main.py input.txt
```

Example content of `input.txt`:

```
1 -3 2
```

This will solve the equation `x^2 - 3x + 2 = 0`.

## File Format for Non-Interactive Mode

The input file should contain a single line with three space-separated real numbers:

```
a b c
```

Where:
- `a` must not be `0`
- `b` and `c` are any real numbers

Example:

```
1 2 -3
```

This represents the equation `x^2 + 2x - 3 = 0`.

## Revert Commit
Revert commit was done to undo an improper implementation of the file mode. Error handling was added later.

[Link to the Revert Commit]()
