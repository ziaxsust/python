def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest
    Formula: SI = (P * R * T) / 100
    """
    si = (principal * rate * time) / 100
    return si


def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculate Compound Interest
    Formula: CI = P * (1 + R/n*100)^(n*t) - P
    n = number of times interest compounded per year
    """
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    ci = amount - principal
    return ci, amount


def get_positive_float(prompt):
    """Input validation - ensures positive numeric input"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Value must be greater than 0. Try again.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def get_compounding_frequency():
    """Let user choose compounding frequency"""
    print("\n📅 Select Compounding Frequency:")
    print("  1. Annually     (n = 1)")
    print("  2. Semi-Annually(n = 2)")
    print("  3. Quarterly    (n = 4)")
    print("  4. Monthly      (n = 12)")
    print("  5. Daily        (n = 365)")

    options = {"1": 1, "2": 2, "3": 4, "4": 12, "5": 365}
    labels  = {"1": "Annually", "2": "Semi-Annually", "3": "Quarterly", "4": "Monthly", "5": "Daily"}

    while True:
        choice = input("\nEnter choice (1-5): ").strip()
        if choice in options:
            return options[choice], labels[choice]
        print("❌ Invalid choice. Please enter a number between 1 and 5.")


def display_results(principal, rate, time, si, ci, final_amount, freq_label):
    """Display all results in a formatted summary"""
    print("\n" + "=" * 50)
    print("        💰 LOAN INTEREST SUMMARY")
    print("=" * 50)
    print(f"  Principal Amount     : ${principal:,.2f}")
    print(f"  Annual Interest Rate : {rate}%")
    print(f"  Time Period          : {time} year(s)")
    print(f"  Compounding          : {freq_label}")
    print("-" * 50)
    print(f"  Simple Interest      : ${si:,.2f}")
    print(f"  Total (SI)           : ${principal + si:,.2f}")
    print("-" * 50)
    print(f"  Compound Interest    : ${ci:,.2f}")
    print(f"  Total (CI)           : ${final_amount:,.2f}")
    print("-" * 50)
    print(f"  💡 Extra paid (CI-SI): ${ci - si:,.2f}")
    print("=" * 50)


def main():
    print("=" * 50)
    print("   🏦 SIMPLE & COMPOUND INTEREST CALCULATOR")
    print("=" * 50)

    # --- Take Inputs ---
    principal = get_positive_float("\nEnter Principal Amount ($): ")
    rate      = get_positive_float("Enter Annual Interest Rate (%): ")
    time      = get_positive_float("Enter Time Period (in years): ")
    n, freq_label = get_compounding_frequency()

    # --- Calculations ---
    si              = calculate_simple_interest(principal, rate, time)
    ci, final_amount = calculate_compound_interest(principal, rate, time, n)

    # --- Display Results ---
    display_results(principal, rate, time, si, ci, final_amount, freq_label)


if __name__ == "__main__":
    main()
