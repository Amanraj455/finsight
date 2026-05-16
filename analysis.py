import pandas as pd

def get_report(data, month):
    df = pd.DataFrame(data, columns=["email","date","category","amount","type"])

    df['date'] = pd.to_datetime(df['date'])
    df = df[df['date'].dt.month == month]

    income = df[df['type'] == 'Income']['amount'].sum()
    expense = df[df['type'] == 'Expense']['amount'].sum()
    savings = income - expense

    expense_df = df[df['type'] == 'Expense']

    if not expense_df.empty:
        category_sum = expense_df.groupby('category')['amount'].sum()
        top_category = category_sum.idxmax()
    else:
        top_category = "No data"
        category_sum = None

    return income, expense, savings, top_category, category_sum