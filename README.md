# Quant-econ

My personal working repository for [QuantEcon](https://quantecon.org/): lecture exercises, solutions, and notes from working through quantitative economics with Python.

This is a learning repo, not a library. Code here is written to understand the material, so it favours clarity over performance and gets rewritten as I learn better ways to do things.

---

## What's in here

Work is organised by lecture section.

### 1. An introductory example

| File | What it does |
|------|--------------|
| `first.py` | Plots 100 draws from the standard normal |
| `second.py` | Same plot built with an explicit loop and a list |
| `third.py` | Compound interest on a bank balance over 50 periods |
| `exercise_1.py` | Simulates and plots the AR(1) series `x[t+1] = a*x[t] + e` |
| `exercise_1.2.py` | The same series overlaid for `a = 0, 0.8, 0.98` |
| `exercise_2.py` | AR(1) variant using the absolute value of the previous term |
| `exercise_2.1.py` | The same variant written with an explicit if/else |
| `exercise_2.2.py` | Monte Carlo approximation of pi from 1,000,000 random points |

### 2. Functions

| File | What it does |
|------|--------------|
| `4.3.4.py` | Numerical integration of `x**3` with `scipy.integrate.quad` |
| `4.4.1.py` | Builds a time series of normal draws in a loop, then plots it |
| `4.4.2.py` | Generalises that into a function that switches between uniform and normal draws |
| `4.5.1.py` | Computes powers of 2 with a loop |
| `4.5.2.py` | The same result in one line with the `**` operator |

### 2. Functions, 4.6 Exercises

| File | What it does |
|------|--------------|
| `binomial_vari.py` | Draws a binomial random variable, built from uniform draws rather than a library call |
| `Coin.py` | Flips 10 coins and scans for runs of three heads or three tails |
| `Factorial.py` | Factorial with a for loop |
| `Factorial2.py` | Factorial with a while loop |

### 2. Functions, 4.7 Advanced Exercise

| File | What it does |
|------|--------------|
| `fectorial.py` | Factorial written recursively, with a base case at 0 and 1 |
| `fibonacci.py` | Fibonacci written recursively |

---

## Topics covered

Checked off as I complete them.

- [x] Python basics: data types, control flow, loops
- [x] Writing functions, arguments and return values
- [x] Recursion and base cases
- [x] NumPy arrays and the `default_rng` random generator
- [x] Matplotlib and visualisation
- [x] Random simulation: AR(1) series, coin flips, Monte Carlo
- [ ] Vectorised computation (replacing loops with array operations)
- [ ] SciPy: optimisation, interpolation, linear algebra
- [ ] Pandas for economic data
- [ ] Linear algebra and matrix methods
- [ ] Markov chains
- [ ] Finite-state dynamic programming
- [ ] Job search and the McCall model
- [ ] Asset pricing
- [ ] Time series and filtering

---

## Running the code

Requires Python 3.10 or newer.

```bash
# install the core scientific stack
pip install numpy scipy matplotlib pandas quantecon

# run a script
python "1.An introductory example/first.py"
```

For notebooks:

```bash
pip install jupyterlab
jupyter lab
```

If you prefer an isolated environment:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS / Linux
pip install numpy scipy matplotlib pandas quantecon
```

---

## Source material

- [QuantEcon lectures](https://quantecon.org/lectures/): the lecture series this work follows
- [Python Programming for Economics and Finance](https://python-programming.quantecon.org/)
- [Quantitative Economics with Python](https://python.quantecon.org/)
- [QuantEcon.py documentation](https://quanteconpy.readthedocs.io/)

---

## Notes

Solutions here are my own attempts. Where they differ from the official QuantEcon solutions, that's usually me working something out the long way first, and I try to note it in comments when I know the difference.

Lecture content and the official solutions belong to the QuantEcon project and its authors.
