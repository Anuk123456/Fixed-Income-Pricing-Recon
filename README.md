Fixed Income Pricing, Risk Analytics & Automated PnL Reconciliation Engine

Object-oriented pricing and risk engine for fixed-income instruments, paired with an automated PnL reconciliation test suite built to catch trade discrepancies and desk anomalies.

What it does:
- Computes exact Macaulay duration, Modified duration, DV01, and convexity profiles for synthetic instruments within strict tolerance thresholds.
- Reconciles internal trade books against independent vendor feeds across multi-category error controls (missing feeds, valuation discrepancies, notional mismatches).
- Automated unit testing via pytest ensuring 100% test pass rates and robust exception detection.

How to run the tests:
Make sure pandas and pytest are installed, then run:
python -m pytest
