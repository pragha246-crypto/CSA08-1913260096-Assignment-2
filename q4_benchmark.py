"""Q4: Benchmark several string-building strategies (times vary by machine)."""
import io
import timeit

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return ";".join(parts) + ";" if parts else ""

def build_stringio(parts):
    buf = io.StringIO()
    for p in parts:
        buf.write(p)
        buf.write(";")
    return buf.getvalue()

def build_plus_slow(parts):
    text = ""
    for p in parts:
        text = text + p + ";"
    return text

def main():
    parts = [f"Item{i}:Rs{i % 50}" for i in range(20000)]
    methods = [("+= loop", lambda: build_plus(parts)),
               ("join", lambda: build_join(parts)),
               ("StringIO", lambda: build_stringio(parts)),
               ("plain + loop", lambda: build_plus_slow(parts))]
    expected = build_join(parts)
    print("Q4 - Benchmark (best of 3; local timings)")
    for name, fn in methods:
        assert fn() == expected
        elapsed = min(timeit.repeat(fn, number=1, repeat=3))
        print(f"{name:14}: {elapsed:.6f} s")

if __name__ == "__main__":
    main()
