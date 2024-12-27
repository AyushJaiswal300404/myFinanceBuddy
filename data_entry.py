from datetime import datetime
date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}
def get_date(prompt, allow_default=False):
    date_format = "%d-%m-%Y"
    date_str = input(prompt)
    if allow_default and date_str == "":
        return datetime.now().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter a date in the format dd-mm-yyyy")
        return get_date(prompt, allow_default)
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError:
        print("Invalid input. Please enter a valid number greater than 0.")
        return get_amount()
def get_category():
    category = input("Enter the category ('I' for income or 'E' for expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense")
    return get_category()
def get_description():
    return input("Enter the description: ")