# Quant-econ

My personal working repository for [QuantEcon](https://quantecon.org/): lecture exercises, solutions, and notes from working through quantitative economics with Python.

This is a learning repo, not a library. Code here is written to understand the material, so it favours clarity over performance and gets rewritten as I learn better ways to do things.

---

## What's in here

| Path | What it is |
|------|------------|
| `first.py` | Starting point / scratch file |

---

## Topics covered

Checked off as I complete them.

- [ ] Python basics: data types, control flow, functions
- [ ] NumPy and vectorised computation
- [ ] Matplotlib and visualisation
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
python first.py
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
