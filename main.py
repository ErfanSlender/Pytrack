# Libabry
import json
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
#print(today)
# Functions

def show_menu():
    print('\n1.Add Income')
    print('2.Add Expense')
    print('3.Show Balance')
    print('4.Show Transactions')
    print('5.Delete Transactions')
    print('6.Search Transactions')
    print('7.Expense Report')
    print('8.Filter Transactions by Month')
    print('9.Edit Transaction')
    print('10.Exit')
    
def load_transactions():
    try:
        with open('transactions.json', 'r') as file:
         return json.load(file)
    except FileNotFoundError:
        return []

def save_transactions(transactions):
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file, indent=4)
        
def calculate_balance(transactions):
    total_income = 0
    total_expense = 0
            
    for transaction in transactions:
        if transaction['Type'] == 'Income':
            total_income += transaction['Amount']
        elif transaction['Type'] == 'Expense':
            total_expense += transaction['Amount']
    return  total_income, total_expense

def get_valid_amount(message):
    while True:
        try:
            amount = int(input(message))
            if amount <= 0:
                print('Amount must be greater than Zero!')
                continue
            return amount
        except ValueError:
            print('Please enter a number!')

def get_valid_category():
    while True:
        category = input('Enter Category: ').strip()
        if not category:
            print('Category cannot be empty!')
            continue
        return category

def show_transations(transactions):
    if not transactions:
        print('No transations found!')
    else:
        for index, transaction in enumerate(transactions, start=1):
            print(index, transaction)

def delete_transaction(transactions):
    if not transactions:
        print('No transactions found!')
        return
    show_transations(transactions)
    try:
        choice = int(input('Enter transaction number to delete: '))
    except ValueError:
        print('Please enter a valid number!')
        return
    index = choice - 1
    if index < 0 or index >= len(transactions):
        print('Invalid transaction number!')
        return
    deleted_transaction = transactions.pop(index)
    save_transactions(transactions)
    print('Transaction deleted successfully!')
    print(deleted_transaction)
    
def search_transactions(transactions):
    found = False
    category = input('Enter Category: ').strip()
    for transaction in transactions:
        if transaction['Category'] == category:
            print(transaction)
            found = True
    if not found:
        print('No transactions found!')
    
def expense_report(transactions):
    expenses_by_category = {}
    for transaction in transactions:
        if transaction['Type'] == 'Expense':
            category = transaction['Category']
            amount = transaction['Amount']
            expenses_by_category[category] = (
                
                expenses_by_category.get(category, 0) + amount
                
                )
    
    print('\n============ Expense Report ============')
    for category, amount in expenses_by_category.items():
        print(f'{category}: {amount}')
        
    print('-----------------------------------------') 
    
def filter_transactions_by_month(transactions):
    while True:
        month = input('Enter month (YYYY-MM): ')
        try:
            datetime.strptime(month, '%Y-%m')
            break
        
        except ValueError:
            print('Invalid date format! Example: 2026-10')
            
    found = False
    
    for transaction in transactions:
        transaction_date = transaction.get('Date', '')
        if transaction_date.startswith(month):
            print(transaction)
            found = True
    if not found:
        print('No transaction found for this month!')
        
def edit_transaction(transactions):
    if not transactions:
        print('No transactions found!')
        return
    show_transations(transactions)
    try:
        choice = int(input('Enter transaction number to edit: '))
    except ValueError:
        print('Please enter a valid Number!')
        return
    index = choice - 1
    if index < 0 or index >= len(transactions):
        print('InValid transaction number!')
        return
    
    transaction = transactions[index]
    
    print('1.Edit Amout')
    print('2.Edit Category')
    
    edit_choice = input('What do you want to edit? ')
    
    if edit_choice == '1':
        transaction['Amount'] = get_valid_amount('Enter new amount: ')
    elif edit_choice == '2':
        transaction['Category'] = get_valid_category()
    else:
        print('Invalid choice!')
        return
    
    save_transactions(transactions)
    
    print('Transaction update successfully!')

#transactions = load_transactions()
        



income = 0
expense = 0
balance = 0
today = ''
category_income = ''
category_expense = ''
amount = 0

def main():
    print('Welcome to PyTrack!')

    transactions = load_transactions()
    
    while True:
        show_menu()
        
        choice = input('Enter your choice: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ')
        if choice == '1':
            print('You selected Add Income.')
            amount = get_valid_amount('Enter your Income: ')
            income += amount
            category_income = get_valid_category()
            today = datetime.now().strftime('%Y-%m-%d')
            transactions.append({
                'Type': 'Income',
                'Amount': amount,
                'Category': category_income,
                'Date': today
                })
            save_transactions(transactions)
            print('Income added successfully!')
        elif choice == '2':
            print('You selected Add Expense')
            amount = get_valid_amount('Enter your Expense: ')
            category_expense = get_valid_category()
            today = datetime.now().strftime('%Y-%m-%d')
            transactions.append({
                'Type': 'Expense',
                'Amount': amount,
                'Category': category_expense,
                'Date': today
            })
            save_transactions(transactions)
            print('Expense added successfully!')
        elif choice == '3':
            
            total_income, total_expense = calculate_balance(transactions)
            balance = total_income - total_expense
            
            print(f'Total Income: {total_income}')
            print(f'Total Expense: {total_expense}')
            print(f'Your Balance is: {balance}')
        elif choice == '4':
            print('\n=========== TRANSACTIONS ===========')
            if not transactions:
                print('No transactions found!')
            else:
                for transaction in transactions:
                    print(f'Type: {transaction['Type']}')
                    print(f'Amount: {transaction['Amount']}')
                    print(f'Catergory: {transaction['Category']}')
                    print(f'Date: {transaction.get('Date', 'Unknown')}')
                    print('----------------------------------')
        elif choice == '5':
            print('You selected Edit Transactions')
            delete_transaction(transactions)
        elif choice == '6':
            search_transactions(transactions)
        elif choice == '7':
            expense_report(transactions)
        elif choice == '8':
            filter_transactions_by_month(transactions)
        elif choice == '9':
            edit_transaction(transactions)
        elif choice == '10':
            print('You selected (Exit), GoodBye :)')
            break
        else:
            print('Invalid Choice')

if __name__=='__main__':
    main()