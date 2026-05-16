import streamlit as st
from db import add_transaction

st.set_page_config(layout="wide")

st.title("➕ Add Transaction")


if not st.session_state.get("logged_in", False):
    st.warning("Please login from Home page.")
    st.stop()

email = st.session_state.user_email


st.markdown("""
<style>
.block-container {
    max-width: 700px;
    margin: auto;
}

/* spacing fix */
.stTextInput, .stNumberInput, .stTextArea, .stSelectbox, .stDateInput {
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.write("")


with st.container(border=True):

    date = st.date_input("Date")

    t_type = st.selectbox("Type", ["Income", "Expense"])

    
    if t_type == "Expense":
        category = st.selectbox(
            "Category",
            ["Food 🍕", "Travel ✈️", "Shopping 🛍️", "Other"]
        )
    else:
        category = st.selectbox(
            "Category",
            ["Salary 💰", "Freelance 💻", "Business 📈", "Other"]
        )

    amount = st.number_input("Amount", min_value=0.0, step=1.0)

    desc = st.text_area("Description")

    
    if st.button("➕ Add Transaction", use_container_width=True):
        if amount == 0:
            st.warning("Please enter amount")
        else:
            add_transaction(email, str(date), category, amount, t_type)
            st.success(f"{t_type} Added Successfully ✅")