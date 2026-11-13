"""Q1: Electricity subsidy decisions; compare separate ifs with if-elif-else."""

HOUSEHOLDS = [
    (50, True, False), (100, False, False), (100, True, False),
    (101, True, False), (101, False, False), (200, True, False),
    (201, True, False), (250, False, True),
]

def subsidy_separate_if(units, ration_card, senior):
    # Deliberately independent conditions: illustrates overlapping decisions.
    decisions = []
    if units <= 100:
        decisions.append("FULL")
    if 101 <= units <= 200 and ration_card:
        decisions.append("PARTIAL")
    if units > 200 and senior:
        decisions.append("SENIOR")
    if not decisions:
        decisions.append("NONE")
    return " + ".join(decisions)

def subsidy_lookup(units, ration_card, senior):
    slabs = [
        (100, lambda: "FULL"),
        (200, lambda: "PARTIAL" if ration_card else "NONE"),
        (float("inf"), lambda: "SENIOR" if senior else "NONE"),
    ]
    for upper, decide in slabs:
        if units <= upper:
            return decide()

def subsidy(units, ration_card, senior):
    if units <= 100:
        return "FULL"
    elif 101 <= units <= 200 and ration_card:
        return "PARTIAL"
    elif units > 200 and senior:
        return "SENIOR"
    else:
        return "NONE"

def main():
    print("Q1 - Electricity Subsidy Decisions")
    print("No. Units Ration Senior Correct Separate-if")
    for i, (units, ration, senior) in enumerate(HOUSEHOLDS, 1):
        print(f"{i:>2}  {units:>5} {str(ration):>6} {str(senior):>6} "
              f"{subsidy(units, ration, senior):>8} {subsidy_separate_if(units, ration, senior)}")
    print("\nBoundary checks:", {u: subsidy(u, True, False) for u in (100, 101, 200, 201)})
    print("Lookup agrees:", all(subsidy(*h) == subsidy_lookup(*h) for h in HOUSEHOLDS))

if __name__ == "__main__":
    main()
