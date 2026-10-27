# TIP CALCULATOR

bill = float(input("What was the total bill? $"))
tip_percent = float(input("What tip percentage would you like to give? "))
people = int(input("How many people will split the bill? "))

if bill < 0 or people <= 0 or tip_percent < 0:
    print("Please enter a non-negative bill/tip and at least one person.")
else:
    total = bill * (1 + tip_percent / 100)
    per_person = total / people

    print(f"Total including tip: ${total:.2f}")
    print(f"Each person pays: ${per_person:.2f}")