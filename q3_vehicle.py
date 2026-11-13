"""Q3: Normalise and validate Indian-style vehicle registration strings."""
import re

def normalise(raw):
    return "".join(raw.upper().split()).replace("-", "")

def is_valid_slicing(reg):
    if not reg.isascii() or len(reg) not in (9, 10):
        return False
    state, district = reg[:2], reg[2:4]
    series, number = reg[4:-4], reg[-4:]
    return (state.isalpha() and district.isdigit()
            and len(series) in (1, 2) and series.isalpha()
            and number.isdigit())

def is_valid_regex(reg):
    return bool(reg.isascii() and re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg))

def format_reg(reg):
    if not is_valid_slicing(reg):
        return "INVALID"
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"

def main():
    tests = ["mh 12 c 4567", "ap39-bz-9999", "T N-0 9-A B-12 34",
             "DL-8-CAF-5030", "TN09AB1234", "TN9AB1234", "²N09AB1234"]
    print("Q3 - Vehicle Registration Validator")
    for raw in tests:
        reg = normalise(raw)
        print(f"{raw!r:24} -> {reg:12} -> {format_reg(reg)}")
    print("Slicing and regex agree:", all(is_valid_slicing(normalise(x)) == is_valid_regex(normalise(x)) for x in tests))

if __name__ == "__main__":
    main()
