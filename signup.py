import streamlit as st


st.image("images\golden-logo-template-free-png.webp", width=80)
st.title("Create Your Account ")
st.write("Join our Tech Camp community and start your learning journey.")
st.divider()

# BODY
with st.form("signup_form"):
    st.subheader("Personal Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        full_name = st.text_input("Full Name *", placeholder="e.g. Ahmed Mohamed")
        email = st.text_input("Email Address *", placeholder="example@mail.com")
        password = st.text_input("Password *", type="password", placeholder="Enter secure password")

        
    with col2:
        phone = st.text_input("Phone Number *", placeholder="+20 1xx xxxx xxx")
        address = st.text_input("Address", placeholder="Street, City, Country")
        confirm_password = st.text_input("Confirm Password *", type="password", placeholder="Confirm password")

    submit_button = st.form_submit_button("Create Account", use_container_width=True)

if submit_button:
    if not full_name or not email or not phone or not password or not confirm_password:
        st.error("Please fill in all required fields marked with (*)")
    elif password != confirm_password:
        st.error("Passwords do not match. Please try again.")
    else:
        st.session_state["full_name"] = full_name
        st.session_state["email"] = email
        st.session_state["phone"] = phone
        st.session_state["password"] = password
        
        st.success("Account created successfully!")
st.divider()

st.write("Already have an account?")
if st.button("Go to Login"):
    st.switch_page("signin.py")