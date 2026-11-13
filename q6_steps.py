"""Q6: Ways to climb n steps using 1 or 2 steps at a time."""
from functools import lru_cache
import sys
import timeit

naive_calls = 0

def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_loop(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    prev, cur = 1, 1
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur
    return cur

def main():
    global naive_calls
    print("Q6 - Temple Steps")
    print("n  naive  memo  loop")
    for n in range(1, 7):
        naive_calls = 0
        a = ways_naive(n)
        ways_memo.cache_clear()
        b = ways_memo(n)
        c = ways_loop(n)
        print(f"{n}  {a:5}  {b:5}  {c:5}")
    naive_calls = 0
    ways_naive(30)
    ways_memo.cache_clear()
    ways_memo(30)
    print("naive calls at n=30:", naive_calls)
    print("memoised cache entries at n=30:", ways_memo.cache_info().currsize)
    try:
        ways_memo.cache_clear()
        print("memo(1000):", len(str(ways_memo(1000))), "digits")
    except RecursionError as exc:
        print("memo(1000) recursion limit:", type(exc).__name__)
    loop_value = ways_loop(1000)
    print("loop(1000) digits:", len(str(loop_value)))
    # Raise the limit only for this optional cross-check; deployment uses the loop.
    sys.setrecursionlimit(3000)
    ways_memo.cache_clear()
    print("loop and memo agree at 1000:", loop_value == ways_memo(1000))

if __name__ == "__main__":
    main()
