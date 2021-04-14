#import required libabraries
import streamlit as st
import numpy as np
import streamlit.components.v1 as components
import smtplib, ssl
import base64

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "info@aisoftwaresolutions.io"  # Enter your address
receiver_email = "aisoftwaresolutions.info@gmail.com"  # Enter receiver address
password = "Mallamma.1"
#Settings

# #background image 
# main_bg = "sample.jpg"
# main_bg_ext = "jpg"



# st.markdown(
#     f"""
#     <style>
#     .reportview-container {{
#         background: url(data:{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
#     }}
   
#     </style>
#     """,
#     unsafe_allow_html=True
# )

#title
st.title("AI Software Solutions")
st.markdown(""" ###### _ We Build Fast, To make you smile _""")


#Side bar details
st.sidebar.image("logo.png",width=220)

st.sidebar.markdown(""" ## AI Software Solutions
###### _ We Build Fast, To make you smile _
### Address & Contact Info
### AI Software Solutions
#### 98 Kärrhöksgatan,55612 Sweden  
#### _ :email: info@aisoftwaresolutions.io _
#### _ :phone: +46 - 764439519 _
#### _ [Instagram](https://www.instagram.com/iamnikhilramesh/)  [Linkedin](https://www.linkedin.com/in/nikhil-ramesh-5125b7139/)  [Github](https://github.com/Iamnikhilramesh) _

 """)


def mail():
    st.title("Contact us")
    name,email = st.beta_columns([6,13])
    service, message = st.beta_columns([6,10])
    name = name.text_input("Your Name")
    service = service.selectbox("Select Required Service",['Data Application','Machine Learning Application','ETL Solution',"Artificial Intelligence Application","Others"])
    email = email.text_input("Your Email")
    message = message.text_input("Your Message")
    return name,email,message,service

#Function to display home page
def home():
    st.header("Our Mission and Goal")
    st.text_area("The passionate team who are ready to take up any challenging task and complete it on time,
                        AI should be a benefit for our society and everyone in the society.")
    st.markdown(""" ## Our Core Values
    #### _ Passion, Commitment, Positivity, Honesty and Growth _
    """)
    st.markdown(""" ## Our Core Principles
    #### _ As we follow a agile workflow, our core principles are Individuals and interactions, Working software, Customer collaboration and Responding to change. _
    
    """)
    # mission = st.beta_expander("Our Mission and Goal ", expanded=True)
    # with mission:
    #     st.text("Our Mission and Goal")
    
    # values = st.beta_expander("Core Values ", expanded=True)
    # with values:
    #     st.text("Core Values")
    
    # principles = st.beta_expander("Core Principles ", expanded=True)
    # with principles:
    #     st.text("Core Principles")
    st.text("")
    my_expander = st.beta_expander("Some of the Clients We have worked with", expanded=True)
    with my_expander:
        d,e = st.beta_columns(2)
        d.image("isha.jpeg",caption="Isha Foundations")
        e.image("nccab.png",caption="NCC AB")
        f,g = st.beta_columns(2)
        f.image("kmc.jpeg",caption="Kaveri Medical Center")
        g.image("luxin.png",caption="Luxin Group AB")
        a,b = st.beta_columns(2)
        a.image("agile.png", caption="Agile Health")
        b.image("aj.png",caption="A J Hospital")
        c,h = st.beta_columns(2)
        c.image("employchain.jpeg",caption="Employchain AB")
    
    team = st.beta_expander("Team ", expanded=True)
    with team:
        st.text("")
        st.markdown(""" ### Nikhil Ramesh""")
        st.markdown("""#### _ Founder & CEO _
        """)
        st.image("photo.jpeg",width=140)
        st.markdown("""#### [Linkedin](https://www.linkedin.com/in/nikhil-ramesh-5125b7139/) [Github](https://github.com/Iamnikhilramesh) """)
    
    my_expander_p = st.beta_expander("Some of the Projects We have worked with", expanded=True)
    with my_expander_p:
        a,b = st.beta_columns(2)
        a.image("leaf.jpeg",caption="Leaf Feature Extraction (2017)")
        a.markdown("""[Click here to know more](https://www.youtube.com/)""")
        b.image("Hospital.jpeg", caption="Hospital managament System (2018)")
        b.markdown("""[Click here to know more](https://www.youtube.com/)""")
        c,d = st.beta_columns(2)
        c.image("LIS.png",caption="Lab Information System and Radiology Information System (2018)")
        c.markdown("""[Click here to know more](https://www.youtube.com/)""")
        d.image("allergy.jpeg",caption="Allergen Identification(2019)")
        d.markdown("""[Click here to know more](https://www.youtube.com/)""")
        e,f = st.beta_columns(2)
        e.image("doctor.jpeg",caption="Doctor Appointment Application (2019)")
        e.markdown("""[Click here to know more](https://www.youtube.com/)""")
        f.image("jobmatch.jpeg",caption="Job Matching App (2020)")
        f.markdown("""[Click here to know more](https://www.youtube.com/)""")
        g,h = st.beta_columns(2)
        g.image("lane.jpeg",caption="Lane Detection for self driving car (2020)")
        g.markdown("""[Click here to know more](https://www.youtube.com/)""")
        h.image("treeclasify.jpeg",caption="Tree classification using CNN (2020)")
        h.markdown("""[Click here to know more](https://www.youtube.com/)""")
        i, j= st.beta_columns(2)
        i.image("bim.jpeg",caption="BIM Class Detection Bot (2021)")
        i.markdown("""[Click here to know more](https://www.youtube.com/)""")
    
    name,email,message,service = mail()
    message = """
    Subject: AI Software Solutions Message

    This message is sent from Website""" + "Name : " + name + ", email : "+ email + ", Required Service :" + service + ", Message : " + message
    if st.button('Submit'):
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            st.success("Thank you for your request, Will get back to you soon")
        except Exception as e:
            print(e)

    events = st.beta_expander("Events ", expanded=True)
    with events:
        st.text("There are no upcoming Events")
    

#to Navigate the functions defined as page.
try:
    home()
except Exception as e:
    print(e)


#Goal 
#Passionate team who are ready to take up any challenging task and complete on time, 
# 

#Mission 
# Our Mission is to build smart application which makes everyones life easy.

# Core Values
# Passion, Commitment, Positivity, Honesty and Growth

#Core principles
# As we follow a agile workflow, our core principles are Individuals and interactions, 
# Working software, Customer collaboration and Responding to change.

