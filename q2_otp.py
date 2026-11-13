"""Q2: OTP verification with loop control and recursion comparison."""
OTP = "4821"

def verify_while(entries, limit=3):
    attempts = 0
    for entry in entries:
        if attempts >= limit:
            break
        if not entry.strip():
            continue
        attempts += 1
        if entry.strip() == OTP:
            return f"VERIFIED ({attempts})"
        pass  # placeholder: no extra action for an incorrect OTP
    else:
        return f"LOCKED ({attempts})"
    return f"LOCKED ({attempts})"

def verify_for(entries, limit=3):
    attempts = 0
    for entry in entries:
        if attempts == limit:
            break
        if not entry.strip():
            continue
        attempts += 1
        if entry.strip() == OTP:
            return f"VERIFIED ({attempts})"
    else:
        return f"LOCKED ({attempts})"
    return f"LOCKED ({attempts})"

def verify_recursive(entries, index=0, attempts=0, limit=3):
    if index >= len(entries) or attempts >= limit:
        return f"LOCKED ({attempts})"
    value = entries[index].strip()
    if not value:
        return verify_recursive(entries, index + 1, attempts, limit)
    attempts += 1
    if value == OTP:
        return f"VERIFIED ({attempts})"
    return verify_recursive(entries, index + 1, attempts, limit)

def main():
    scenarios = {
        "correct first": ["4821"],
        "blank entries then correct": ["", " ", "4821"],
        "three wrong": ["1111", "2222", "3333"],
        "two wrong then correct": ["1111", "2222", "4821"],
        "three wrong then correct": ["1111", "2222", "3333", "4821"],
    }
    print("Q2 - OTP Verification")
    for name, entries in scenarios.items():
        print(f"{name:28} while={verify_while(entries):18} for={verify_for(entries):18} recursion={verify_recursive(entries)}")

if __name__ == "__main__":
    main()
