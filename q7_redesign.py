"""Q7: Diagnose exponential recursion and validate an O(n), O(1)-space redesign."""
from functools import lru_cache
import csv
from pathlib import Path
import sys

calls = 0
def ways_original(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_original(n - 1) + ways_original(n - 2)

def ways_redesign(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    prev, cur = 1, 1
    additions = 0
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur
        additions += 1
    return cur, additions

@lru_cache(maxsize=None)
def ways_memo(n):
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def main():
    global calls
    print("Q7 - Redesign and Validation")
    print("n  original calls  redesign additions  same answer")
    for n in (5, 10, 20, 25, 30):
        calls = 0
        original = ways_original(n)
        redesigned, additions = ways_redesign(n)
        print(f"{n:2} {calls:15} {additions:19} {original == redesigned}")
    ways_memo.cache_clear()
    try:
        ways_memo(1000)
        memo_status = "completed"
    except RecursionError:
        memo_status = "RecursionError at default recursion limit"
    redesigned, additions = ways_redesign(1000)
    print("memoised n=1000:", memo_status)
    print("redesign n=1000 additions:", additions)
    # Optional validation with a raised limit; the redesign itself does not need it.
    sys.setrecursionlimit(3000)
    ways_memo.cache_clear()
    print("redesign n=1000 equals memo:", redesigned == ways_memo(1000))
    print("Design: O(n) additions, O(1) extra memory; no recursive call stack.")

if __name__ == "__main__":
    main()
