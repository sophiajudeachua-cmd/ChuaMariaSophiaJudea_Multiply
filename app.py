def multiply_two_numbers():
    print("┌──────────────────────────────────────┐")
    print("│           NUMBER MULTIPLIER          │")
    print("└──────────────────────────────────────┘")

    try:
        ChuaNum1 = float(input("  Input First Number  : "))
        ChuaNum2 = float(input("  Input Second Number : "))

        ChuaResult = ChuaNum1 * ChuaNum2

        print("  " + "═" * 36)
        print(f"  RESULT: {ChuaNum1} × {ChuaNum2} = {ChuaResult}")
        print("  " + "═" * 36)
    except ValueError:
        print("  [!] Error: Invalid numeric input.")

if __name__ == "__main__":
    multiply_two_numbers()