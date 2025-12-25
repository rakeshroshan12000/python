def main():
    expense = {}
    print("1. Add expense")
    print("2. Show summary")
    print("3. Exit")
    choice = input("Chose an option:")
    while True:
        if choice == '1':
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            expense[name] = amount
            print("Expense added successfully.")
        elif choice == '2':
            if not expense:
                print("No expenses found.")
            else:
                print("Expense Summary:")
                for name, amount in expense.items():
                    print(f"{name}: {amount}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        choice = input("Choose an option:")

if __name__ == "__main__":
    main()

