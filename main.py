from prof_elec_4.decision_tree import *

if __name__ == "__main__":
    lst = [
        DT(True, "single", 125000),
        DT(False, "married", 100000),
        DT(True, "single", 70000),
        DT(True, "married", 120000),
        DT(False, "divorced", 95000),
    ]

    people = People()

    for i in lst:
        people.insert(i)
