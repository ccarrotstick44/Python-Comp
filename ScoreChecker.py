while True:
    score = int(input("Enter your test score: "))

    if score > 100:
        print("Invalid test score--ERROR234B")
    elif score >= 90:
        print("You have received an S")
    elif score >= 85:
        print("You received an A+")
    elif score >= 80:
        print("You have received an A")
    elif score >= 70:
        print("You have received a B")
    elif score >= 60:
        print("You have received a C")
    elif score >= 50:
        print("You have received a D")
    else:
        print("Unfortunately, you have not passed the examination")
