import streamlit as st


def about_me():

    #About me
    my_expander3 = st.beta_expander("A few words about me", expanded=True)
    with my_expander3:
        st.markdown("""## _ __ I’m Nikhil Ramesh, a multidisciplinary thinker who focuses on telling my clients’ stories with statistics, through enjoyable and meaningful experiences. I specialize in Machine learning algorithms, Data Pipelines and Data visualization tools. __ _""")
        st.markdown("""### _ Over the past 4 years I have been working with companies and startups around the world as a developer and Data Scientist, working solo and leading small smart application. _ """)
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