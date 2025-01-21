import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portfolio", page_icon="🌟", layout="wide")

try:
    shared_img = Image.open("pic.jpg")
except FileNotFoundError:
    st.error("Profile picture file not found. Please ensure 'pic.jpg' exists in your working directory.")
    shared_img = None

page = st.sidebar.radio("Navigate", ["Home", "About", "Projects", "Skills", "Contact"])

def home_layout():
    col1, col2 = st.columns([1, 3])
    with col1:
        if shared_img:
            st.image(shared_img, width=150, use_column_width=False, caption="Imad Subhan")
        else:
            st.write("")
    with col2:
        home_content()

def home_content():
    st.title("🌟 Welcome to My Portfolio")
    st.header("Name: Imad Subhan")
    st.write("**Introduction:**")
    st.write("I am a passionate and results-driven Data Science student with a strong academic foundation in data analysis and statistical modeling. Skilled in Python, R, SQL, and data visualization tools like Tableau and Power BI, I excel at extracting meaningful insights from complex datasets to solve real-world problems.")

def about_content():
    st.title("📖 About Me")
    st.subheader("Education:")
    st.write("**Matric:** Abdali School **Date:** 2018 to 2020")
    st.write("**Intermediate:** Free Engineering **College:** Buner Degree College **Date:** 2020 to 2022")
    st.write("**Bachelor:** Data Science **University:** UCP **Date:** 2022 to 2026")
    st.subheader("Skills:")
    st.write("- Python\n- SQL\n- C++\n- Knime")

def projects_content():
    st.title("💻 My Projects")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Project 1: Visualizing Crime Rates")
        st.write("Description:")
        st.write("A data visualization project analyzing crime rates across major cities.")
        st.write("- Tools: Python, Pandas, Matplotlib, Seaborn.")
        st.write("- Focus: Exploratory Data Analysis and Data Visualization.")
        try:
            project_img = Image.open("crimeimag.jpeg",) 
            st.image(project_img, caption="Project Visualization", use_column_width=True)
        except FileNotFoundError:
            st.write("Project image not found. Add an image named 'project.jpg' to display here.")
        
    with col2:
        st.subheader("Project 2: Bank Account Management System")
        st.write("Description:")
        st.write("An object-oriented programming project simulating basic banking operations.")
        st.write("- Features: Account creation, fund transfer, balance inquiry.")
        st.write("- Tools: Python, OOP concepts.")
        try:
            project_img = Image.open("bankimag.jpeg") 
            st.image(project_img, caption="Project Visualization", use_column_width=True)
        except FileNotFoundError:
            st.write("Project image not found. Add an image named 'project.jpg' to display here.")

def skills_content():
    st.title("🛠️ My Skills")
    skills = {"C++": 90, "Python": 75, "SQL": 80, "Knime": 85}
    for skill, proficiency in skills.items():
        st.write(f"**{skill}**")
        st.progress(proficiency / 100)

def contact_content():
    st.title("📬 My Contact")
    email = st.text_input("Your Email")
    contact_number = st.text_input("Your Phone Number")
    linkedin = st.text_input("LinkedIn Account")
    message = st.text_area("Your Message")
    if st.button("Submit"):
        if email and message:
            st.success("Thank you for reaching out! We will get back to you shortly.")
        else:
            st.error("Please fill out both fields.")

if page == "Home":
    home_layout()
elif page == "About":
    about_content()
elif page == "Projects":
    projects_content()
elif page == "Skills":
    skills_content()
elif page == "Contact":
    contact_content()
