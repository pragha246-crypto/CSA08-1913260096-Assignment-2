# Python Programming Assignment 2

**Student:** Alan Jerry F  
**Register Number:** 1913260096  
**Course:** CSA0821 — Python Programming  
**CO2:** Control Flow, String Operations, Functions and Recursion  
**Slot:** C  
**Environment:** Python 3.12.3 (standard library only)

Repository: https://github.com/pragha246-crypto/CSA08-1913260096-Assignment-2

## Contents
- `Q1/q1_subsidy.py` — electricity subsidy decisions and boundary cases
- `Q2/q2_otp.py` — OTP attempts, blank entries, `while`, `for`, `break`, `continue`, `pass`, loop-else
- `Q3/q3_vehicle.py` — vehicle registration normalisation and validation
- `Q4/q4_build.py` — string building with concatenation and `join()`
- `Q4/q4_benchmark.py` — alternative string-building methods and timings
- `Q5/q5_canteen.py` — default arguments, parameters, return values and scope
- `Q6/q6_steps.py` — recursion, memoisation and iterative solution
- `Q7/q7_redesign.py` — diagnosis, iterative redesign and validation
- `Q7/q7_raw_counts.csv` — operation counts and timing observations
- `outputs/` — captured text output from running the programs

## Run commands
Run from the repository root:
```bash
python Q1/q1_subsidy.py
python Q2/q2_otp.py
python Q3/q3_vehicle.py
python Q4/q4_build.py
python Q4/q4_benchmark.py
python Q5/q5_canteen.py
python Q6/q6_steps.py
python Q7/q7_redesign.py
```

## Results at a glance
- **Q1:** `if-elif-else` gives exactly one subsidy decision, including at 100/101/200/201 units.
- **Q2:** blank OTP entries do not consume an attempt; three incorrect entries lock the account.
- **Q3:** registration strings are normalised and checked against the required state/district/series/number pattern.
- **Q4:** `join()` builds the same text as repeated concatenation and is compared with other approaches.
- **Q5:** using `None` as a default prevents customer orders from sharing one mutable list.
- **Q6:** memoisation avoids repeated recursive work; the iterative solution handles n=1000 without recursion depth changes.
- **Q7:** the bottom-up redesign uses n−1 additions and O(1) extra space, and is checked against the reference recurrence.
