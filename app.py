#import required libabraries
import streamlit as st
import numpy as np
import streamlit.components.v1 as components
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "iamnikhilramesh@gmail.com"  # Enter your address
receiver_email = "nikhilramesh835@gmail.com"  # Enter receiver address
password = "Mallamma.1"
#Settings

#title
st.title("AI Software Solutions")
st.markdown(""" ###### _ We Build Fast, To make you smile _""")


#Side bar details
st.sidebar.title('AI Software Solutions')
st.sidebar.markdown(""" ###### _ We Build Fast, To make you smile _""")

selection = st.sidebar.selectbox("Menu", ["Home","Projects","Get In Touch","About Me"])
st.sidebar.markdown(""" ## Address & Contact Info
### AI Software Solutions
#### 98 Kärrhöksgatan,55612 Sweden  
#### _ :email: iamnikhilramesh@gamil.com _
#### _ :phone: +46 - 764439519 _
#### _ [Instagram](https://www.instagram.com/iamnikhilramesh/) _
#### _ [Linkedin](https://www.linkedin.com/in/nikhil-ramesh-5125b7139/) _
#### _ [Github](https://github.com/Iamnikhilramesh) _

 """)


def mail():
    st.header("Need Assistance ???")
    st.title("Let's work together")
    service = st.selectbox("Select Required Service",['Data Application','Machine Learning Application','ETL Solution',"Artificial Intelligence Application","Others"])
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_input("Your Message")
    return name,email,message,service

#Function to display home page
def home():
    st.header("Home")
#Function to display projects
def projects():
    st.header("Read About Projects")
    my_expander_p = st.beta_expander("Some of the Projects I have worked with", expanded=True)
    with my_expander_p: 
        st.image("leaf.jpeg",caption="Leaf Feature Extraction (2017)")
        st.image("Hospital.jpeg", caption="Hospital managament System (2018)")
        st.image("LIS.png",caption="Lab Information System and Radiology Information System (2018)")
        st.image("allergy.jpeg",caption="Allergen Identification(2019)")
        st.image("doctor.jpeg",caption="Doctor Appointment Application (2019)")
        st.image("jobmatch.jpeg",caption="Job Matching App (2020)")
        st.image("lane.jpeg",caption="Lane Detection for self driving car (2020)")
        st.image("treeclasify.jpeg",caption="Tree classification using CNN (2020)")
        st.image("bim.jpeg",caption="BIM Class Detection Bot (2021)")



#Function to display contact details
def get_in_touch():
    name,email,message,service = mail()
    message = """
    Subject: AI Software Solutions Message

    This message is sent from Website""" + "Name : " + name + ", email : "+ email + ", Required Service :" + service + ", Message : " + message
    if st.button('Submit'):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

#Function to display about me
def about_me():

    #About me
    my_expander3 = st.beta_expander("A few words about me", expanded=True)
    with my_expander3:
        st.markdown("""## _ __ I’m Nikhil Ramesh, a multidisciplinary thinker who focuses on telling my clients’ stories with statistics, through enjoyable and meaningful experiences. I specialize in Machine learning algorithms, Data Pipelines and Data visualization tools. __ _""")
        st.markdown("""### _ Over the past 4 years I have been working with companies and startups around the world as a developer and Data Scientist, working solo and leading small smart application. In my spare time I enjoy travelling and adventures. _ """)
    my_expander = st.beta_expander("Some of the Clients I have worked with", expanded=True)
    with my_expander:
        st.image("agile.png", caption="Agile Health")
        st.image("aj.png",caption="A J Hospital")
        st.image("employchain.jpeg",caption="Employchain AB")
        st.image("isha.jpeg",caption="Isha Foundations")
        st.image("kmc.jpeg",caption="Kaveri Medical Center")
        st.image("nccab.png",caption="NCC AB")
        st.image("luxin.png",caption="Luxin Group AB")
    
    

    my_expander1 = st.beta_expander("Experience", expanded=True)
    with my_expander1:
        st.markdown(""" ### My 4+ years experience, For more details head over to my [linkedin profile](https://www.linkedin.com/in/nikhil-ramesh-5125b7139/)""")
        st.markdown("""| Organization        | Role           | Date  | Place
        | ---------------------------------------------- |:--------------:| -----------------:| -----------------:|
        | BlockchainX AB                                 | Data Scientist | 07/2020 – 12/2020 | Jönköping, Sweden |
        | Agile Health Medexpert Software Solutions      | Junior Software Developer | 08/2018 – 04/2019 | Bangalore, India |
        | Agile Health Medexpert Software Solutions      | Software Engineer | 08/2017 – 07/2018 | Bangalore, India |
        """)
    my_expander2 = st.beta_expander("Skills & Tools", expanded=True)  
    with my_expander2:
        st.markdown(""" Python / Core Java / SQL / AWS / Tableau / KNIME / Machine Learning / Deep Learning / ETL / Object Oriented Programming / Testing and Agile Methodologies / HTML / CSS / JavaScript / Django / Git / MIRTH / Microsoft Office / Postman / Android Studio / Visual Studio code / SQL Developer. """)
    

    images = ['agile.png', 'aj.png', 'employchain.jpeg','isha.jpeg','kmc.jpeg','nccab.png','luxin.png']
    captions = ['Agile Health','A J Hospital','Employchain AB','Isha Foundations','Kaveri Medical Center','NCC AB','Luxin Group AB']


#to Navigate the functions defined as page.
try:
    if selection == "Home":
        home()
    elif selection == "Projects":
        projects()
    elif selection == "Get In Touch":
        get_in_touch()
    elif selection == "About Me":
        about_me()
except Exception as e:
    print(e)
