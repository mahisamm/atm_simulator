
users = {
    '1234': {'name': 'Alice', 'balance': 5000},
    '5678': {'name': 'Bob', 'balance': 3000},
    '0000': {'name': 'Charlie', 'balance': 10000}
}

def login():
    print("=== Welcome to ATM Machine ===")
    pin = input("Enter your 4-digit PIN: ")
    if pin in users:
        print(f"\n✅ Login successful. Welcome, {users[pin]['name']}!")
        atm_menu(pin)
    else:
        print("❌ Invalid PIN. Try again.")
        login()

def atm_menu(pin):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            check_balance(pin)
        elif choice == '2':
            deposit(pin)
        elif choice == '3':
            withdraw(pin)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def check_balance(pin):
    balance = users[pin]['balance']
    print(f"\n💼 Your current balance is: ₹{balance}")

def deposit(pin):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("❌ Invalid amount.")
        else:
            users[pin]['balance'] += amount
            print(f"✅ ₹{amount} deposited successfully.")
            check_balance(pin)
    except ValueError:
        print("❌ Please enter a valid number.")

def withdraw(pin):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("❌ Invalid amount.")
        elif amount > users[pin]['balance']:
            print("❌ Insufficient balance.")
        else:
            users[pin]['balance'] -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
            check_balance(pin)
    except ValueError:
        print("❌ Please enter a valid number.")

# Run the program
login()
