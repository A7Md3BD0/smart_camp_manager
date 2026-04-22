import streamlit as st

home = st.Page("home.py", title="Home", icon="🏠")
signup = st.Page("signup.py", title="Sign Up", icon="👤" , default=True)
signin = st.Page("signin.py", title="Login", icon="🔑")
dashboard = st.Page("dashboard.py", title="Dashboard", icon="📊")
profile = st.Page("profile.py", title="Profile", icon="👤")
contact = st.Page("contact.py", title="Contact", icon="📞")


nav = st.navigation(
    pages=[home,signup,signin,dashboard,profile,contact],
    position="top",
)
nav.run()