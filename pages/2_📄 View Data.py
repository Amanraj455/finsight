import streamlit as st
import pandas as pd
from db import get_data, delete_transaction

st.title("📄 Expense History")


if not st.session_state.get("logged_in", False):
    st.warning("Please login first")
    st.stop()

email = st.session_state.user_email

data = get_data(email)
df = pd.DataFrame(data, columns=["email","date","category","amount","type"])

if df.empty:
    st.info("No transactions yet")
    st.stop()


income_df = df[df['type'] == "Income"]
expense_df = df[df['type'] == "Expense"]

total_income = income_df['amount'].sum()
total_expense = expense_df['amount'].sum()
balance = total_income - total_expense


col1, col2, col3 = st.columns(3)
col1.metric("💰 Income", f"₹{total_income}")
col2.metric("📉 Expense", f"₹{total_expense}")
col3.metric("💵 Balance", f"₹{balance}")

st.write("")


st.subheader("💰 Income Transactions")

if not income_df.empty:
    for i, row in income_df.iterrows():
        c1, c2 = st.columns([8,1])

        with c1:
            st.write(f"{row['date']} | {row['category']} | ₹{row['amount']}")

        with c2:
            if st.button("🗑️", key=f"income_{i}"):
                delete_transaction(
                    row['email'],
                    row['date'],
                    row['category'],
                    row['amount'],
                    row['type']
                )
                st.success("Income Deleted!")
                st.rerun()
else:
    st.info("No income records")


st.subheader("📉 Expense Transactions")

if not expense_df.empty:
    for i, row in expense_df.iterrows():
        c1, c2 = st.columns([8,1])

        with c1:
            st.write(f"{row['date']} | {row['category']} | ₹{row['amount']}")

        with c2:
            if st.button("🗑️", key=f"expense_{i}"):
                delete_transaction(
                    row['email'],
                    row['date'],
                    row['category'],
                    row['amount'],
                    row['type']
                )
                st.success("Expense Deleted!")
                st.rerun()
else:
    st.info("No expense records")


if balance < 0:
    st.error("⚠️ You are overspending!")
elif balance > 0:
    st.success("✅ Good savings!")