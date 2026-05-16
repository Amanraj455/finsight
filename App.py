import streamlit as st
from db import create_tables
from auth import AuthManager

st.set_page_config(page_title="FinSight", layout="wide")
st.markdown("""
<style>

/* Center content */
.block-container {
    max-width: 600px;
    margin: auto;
    padding-top: 3rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1a1d26;
}

/* Tabs spacing */
div[role="tablist"] {
    justify-content: center;
    gap: 30px;
}

/* Input */
input {
    border-radius: 10px !important;
    padding: 12px !important;
}

</style>
""", unsafe_allow_html=True)

create_tables()

st.markdown("""
<style>

/* Sidebar items */
[data-testid="stSidebar"] {
    background-color: #1a1d26;
}

/* Active page highlight */
section[data-testid="stSidebar"] ul li {
    border-radius: 10px;
    padding: 5px;
}

</style>
""", unsafe_allow_html=True)

auth = AuthManager()


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = ""

tab1, tab2 = st.tabs(["🔑 Login", "📄 Register"])


with tab1:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if auth.login_user(email, password):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")


with tab2:
    new_email = st.text_input("New Email")
    new_password = st.text_input("New Password", type="password")

    if st.button("Register"):
        if auth.register_user(new_email, new_password):
            st.success("Registered! Please login")
        else:
            st.error("User already exists")

if st.session_state.logged_in:
    st.success("Go to sidebar → pages")



if st.session_state.logged_in:
    col1, col2 = st.columns([8,2])
    with col2:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            st.rerun()