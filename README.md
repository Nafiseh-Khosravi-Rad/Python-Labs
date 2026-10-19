# Python programming labs

I wrote these college applications in Python, progressing from console programs to object-oriented models and desktop interfaces.

## Lab progression

- Lab-01: billing, books, scores, stock calculations and an interactive story.
- Lab-02: conditions, loops, temperature/currency conversion, mathematical functions and statistics.
- Lab-03: course and employee classes, calculations, rectangle/box inheritance and file-handling exercises.
- Lab-04: collections and PyQt6 interfaces for employee, mathematics and shape exercises.

## Run a console exercise

Install Python 3, then run an exercise directly, for example:

```sh
python Lab-01/BillingProject/billing.py
```

Console exercises prompt for input. Run multi-file exercises from their project directory so local imports and relative file names resolve. Lab-04 GUI modules import PyQt6; install it in a virtual environment before running a GUI entry point. GUI startup was not verified in this publication check.

## Validation

All 43 Python files parsed successfully. Eight volume checks passed across the Lab-03 and Lab-04 box implementations, including a cube, zero and fractional dimensions. The Lab-03 publication copy corrects volume to length × width × height; the original submission is unchanged. These are focused geometry checks, not complete application test coverage.

## Limitations

Employee records and the submitted SQLite database are excluded. Exercises that read those files need a separately prepared synthetic dataset. GUI entry points named test_* are not assumed to be automated tests. Currency conversion exercises use their supplied calculation logic rather than live exchange-rate data.
