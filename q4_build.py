"""Q4: Compare repeated concatenation and str.join()."""
def build_plus(parts):
    text = ""
    for part in parts:
        text += part + ";"
    return text

def build_join(parts):
    return ";".join(parts) + ";" if parts else ""

def main():
    parts = [f"Item{i}:Rs{i % 50}" for i in range(10000)]
    plus = build_plus(parts)
    joined = build_join(parts)
    print("Q4 - String Building")
    print("Same text:", plus == joined)
    print("Length:", len(joined))
    print("Preview:", joined[:100])
    print("join avoids repeatedly creating intermediate strings and is the clearer choice.")

if __name__ == "__main__":
    main()
