import streamlit as st
import pandas as pd
import sqlite3

st.title("🏠 Dashboard")


if not st.session_state.get("logged_in", False):
    st.warning("Please login from Home page.")
    st.stop()

email = st.session_state.user_email


conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM transactions WHERE email=?", conn, params=(email,))


if df.empty:
    st.info("No transactions yet. Start by adding data.")
    st.stop()


income = df[df['type']=="Income"]['amount'].sum()
expense = df[df['type']=="Expense"]['amount'].sum()
savings = income - expense


col1, col2, col3 = st.columns(3)

col1.metric("💰 Income", f"₹{income}")
col2.metric("📉 Expense", f"₹{expense}")
col3.metric("💵 Savings", f"₹{savings}")

st.write("")


st.subheader("📊 Expense Breakdown")

expense_df = df[df['type']=="Expense"]

if not expense_df.empty:
    category_sum = expense_df.groupby("category")["amount"].sum()

    st.bar_chart(category_sum)
else:
    st.info("No expense data available")