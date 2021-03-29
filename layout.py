import streamlit as st


first,second,third = st.beta_columns(3)


first_name = first.text_input("First Name")
middle_name = second.text_input("Middle Name")
last_name = third.text_input("Last Name")

email,mobile = st.beta_columns([3,1])
email_data = email.text_input("Email")
mobile_data = mobile.text_input("Mobile Number")