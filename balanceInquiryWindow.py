#TO BE BUILT SOON

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal

class BalanceInquiryWindow(QWidget):pass
# balance_inquiry.py
def check_balance(balance):
    print("\n===== BALANCE INQUIRY =====")
    print(f"Your current balance is: ₱{balance:.2f}\n")

def main():
    # Example balance value
    balance = 5000.00
    
    user_input = input("Do you want to check your balance? (yes/no): ").lower()

    if user_input == "yes":
        check_balance(balance)
    else:
        print("Balance inquiry cancelled.")

if __name__ == "__main__":
    main()
