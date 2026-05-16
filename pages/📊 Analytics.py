import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.title("📊 Analytics")


if not st.session_state.get("logged_in", False):
    st.warning("Please login from Home page.")
    st.stop()

email = st.session_state.user_email


conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM transactions WHERE email=?", conn, params=(email,))

if df.empty:
    st.info("No data available")
    st.stop()

df['date'] = pd.to_datetime(df['date'])


month = st.slider("Select Month", 1, 12)

df = df[df['date'].dt.month == month]

if df.empty:
    st.warning("No data for this month")
    st.stop()


income = df[df['type']=="Income"]['amount'].sum()
expense = df[df['type']=="Expense"]['amount'].sum()

st.write(f"💰 Income: ₹{income}")
st.write(f"📉 Expense: ₹{expense}")


st.subheader("Expense Distribution")

expense_df = df[df['type']=="Expense"]

if not expense_df.empty:
    category_sum = expense_df.groupby("category")["amount"].sum()

    plt.figure(figsize=(5,5))
    category_sum.plot(kind='pie', autopct='%1.1f%%')
    plt.ylabel("")
    st.pyplot(plt)

    
    top_category = category_sum.idxmax()
    percent = (category_sum.max() / category_sum.sum()) * 100

    st.info(f"⚡ You spend {percent:.1f}% on {top_category}")
else:
    st.info("No expense data")