import csv
import re
from datetime import datetime
CSV_HEADERS  = ["date", "category", "amount", "description"] # an example of the csv headers

'''
Add an expense:
------------------

1. Create a function to prompt the user for expense details. Ensure you ask for:
    1.1. The date of the expense in the format YYYY-MM-DD
    1.2. The category of the expense, such as Food or Travel
    1.3. The amount spent
    1.4. A brief description of the expense
2. Store the expense in a list as a dictionary, where each dictionary includes the date, category, amount, and description as key-value pairs
    Example:
        {'date': '2024-09-18', 'category': 'Food', 'amount': 15.50, 'description': 'Lunch with friends'}

'''

# if isinstance(date_of_expense, str) and date_of_expense != '':

def is_valid_date(date_string):
    try:
        input_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = datetime.today().date()
        return input_date <= today
    except ValueError:
        return False

def get_date_of_expense():
    while True:
        date_of_expense      = input("The date of expense in the format YYYY-MM-DD: ")
        if date_of_expense != '':
            valid_date = is_valid_date(date_of_expense)
            if (valid_date):
                # expenses_dictionary.update({"date":date_of_expense})
                # break
                return date_of_expense
            else:
                print("Not a valid date format. please enter YYYY-MM-DD format")
        else:
            print("date of expenses is empty")

def get_catageory_of_expense():
        while True:
            expense_catageory    = input("The expense category of the expense, such as Food or Travel: ")

            if expense_catageory != '':
                # expenses_dictionary.update({"category":expense_catageory})
                return expense_catageory
                # break
            else:
                print("expenses catageory is empty")

def get_amount_spent():
    while True:
        try:
            amount_spent_expense = float(input("The amount spent: "))
            print(f"amount_spent : {amount_spent_expense}")
            print(f"type of amout_spent : {type(amount_spent_expense)}")
            if amount_spent_expense <= 0:
                continue
            return amount_spent_expense
        except ValueError:
            print(f"you have entered invalid input, please enter valid amount")


def get_description_of_expense():
    while True:
        expenses_description = input("A brief description of the expense :\n\t")

        if expenses_description != '':
            # expenses_dictionary.update({"description":expenses_description})
            return expenses_description
            # break
        else:
            print("Description is empty. please enter valid description.")

def add_expense(expenses_list:list):
    print("Please enter the following details of expenses: \n")
    expenses_dictionary = {}
    
    expenses_dictionary.update({"date":get_date_of_expense()})
    expenses_dictionary.update({"category":get_catageory_of_expense()})
    expenses_dictionary.update({"amount":get_amount_spent()})
    expenses_dictionary.update({"description":get_description_of_expense()})

    print(f"expenses are: \n{expenses_dictionary}")
    expenses_list.append(expenses_dictionary)

def view_expenses(expenses_list:list):
    for expenses in expenses_list:
        if expenses["date"] == '' or datetime.strptime(expenses["date"], "%Y-%m-%d").date() >= datetime.today().date() \
        or expenses["category"] == '' or not isinstance(expenses["category"], str) \
        or expenses["amount"] == None or not isinstance(float(expenses["amount"]), float) \
        or expenses["description"] == '' or not isinstance(expenses["description"], str):
            print("Expenses entry got corrupted/ entry in None")
            # print(expenses)
        else:
            # print(f"found valid expenses")
            print(expenses)

def read_csv(filename:str):
    print(f"Read the : {filename}")
    data = []
    total_expenses = 0.0
    with open(filename, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            total_expenses += float(row["amount"])
            data.append(row)
    
    print(f"total expenses: {total_expenses}")
    return data

def write_csv(filename:str, data:list):
    # print(f"write data: \n{data} \n To file:\n {filename}")
    with open(filename, "w") as file:
        csv_writer = csv.DictWriter(file, CSV_HEADERS)
        csv_writer.writeheader()
        # for row in data:
        csv_writer.writerows(data)


def is_valid_year(year):
    if isinstance(year, int) \
        and year <= datetime.now().year \
            and len(str(year)) == 4:
        return year

def is_valid_month(month):
    if isinstance(month, int) \
    and month > 0 and month <=12:
        return month

def isv_valid_budget(budget):
    if isinstance(budget, float) and budget > 0:
        return budget

def set_monthly_budget():
    year = 0000
    month = 0
    monthly_budget = 0

    while True:
        try:
            year = is_valid_year(int(input("Enter the year you want the budget: ")))
            if not year:
                print(f"Not entered a valid Year... please enter valid <XXXX> year : ")
                continue
            break
        except ValueError:
            print(f"you have entered invalid year type")
    while True:
        try:       
            month = is_valid_month(int(input("Enter the month you want to set the budget: ")))
            if not month:
                print(f"Not entered a valid Month... please enter valid <XX> year : ")
                continue
            break
        except ValueError:
            print(f"you have entered invalid month type")

    while True:
        try:
            monthly_budget = isv_valid_budget(float(input("Enter the total amount they want to budget for the month: ")))
            if not monthly_budget:
                print(f"you have selected budget '{monthly_budget}' which is invalid. please set valid budget")
                continue
            break
        except ValueError:
            print(f"you have entered invalid monthly budget")
    
    return year, month, monthly_budget

def total_expenses_record(target_year:int, target_month:int, budget: float, budget_list:list):
    print("In total expenses record")

    expenses_so_far = 0
    record_found = False
    for item in budget_list:
        if datetime.strptime(item["date"], "%Y-%m-%d").month == target_month \
            and datetime.strptime(item["date"], "%Y-%m-%d").year == target_year:
            expenses_so_far += item["amount"]
            record_found = True
            print(f"{item}")

    if record_found:
        if expenses_so_far > budget:
            print(f"your budget for '{target_year:target_month} is {expenses_so_far} exceeded total {budget}")
        else:
            remaining_budget = budget - expenses_so_far
            print(f"Remaining budget is {remaining_budget}")
    else:
        print(f"No expense record is found for '{target_year}:{target_month}'")

def main():
    print("Expenses tracker program running ...! ")
    expenses_list = read_csv("expenses_data.csv")
    print(f"Main(): data already present: {expenses_list}")

    while True:
        user_choice = int(input("\nselect an option(number(1-5)):\n" \
        "1. Add expenses\n"
        "2. view expenses\n"
        "3. track the budget\n"
        "4. Save expenses to the file\n"
        "5. exit program\n"
        "choice : "))

        # match user_choice:
        #     case 1:
        #         print("In Add expenses.")
        #     case 2:
        #         print("In View expenses.")
        #     case 3: 
        #         print("In track expenses.")
        #     case 4:
        #         print("Save expenses in a file")
        #     case 5:
        #         print("In exit.")
        #         exit()
        #     case _: # This is default case or 
        #         print("Invalid choice please select as shown above.")
        if user_choice == 1:
            print(f"Choise is ==> {user_choice}. add expenses.")
            add_expense(expenses_list)
            print(expenses_list)
        elif user_choice == 2:
            print(f"choice is ==> {user_choice}. view expenses.")
            view_expenses(expenses_list)

        elif user_choice == 3:
            print(f"choice is ==> {user_choice}. track expenses.")
            year, month, month_budget = set_monthly_budget()
            total_expenses_record(year, month, month_budget, expenses_list)
        elif user_choice == 4:
            print(f"choice is ==> {user_choice}. save expenses to a file.")
            # save_expenses()
            write_csv("expenses_data.csv", expenses_list)
        elif user_choice == 5:
            print(f"choice is ==> {user_choice}. save and close / exit from expense tracker.")
            write_csv("expenses_data.csv", expenses_list)
            exit()
        else:
            print("your have selected invalid/incorrect choice. please select (1-5)." \
            "Try Again please ....!\n")


if __name__ == "__main__":
    main()