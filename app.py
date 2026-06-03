import streamlit as st
import pandas as pd
from joblib import load

st.title("AI Career Guidance System")

model = load("career_model.pkl")
target_encoder = load("target_encoder.pkl")

st.header("Student Details")

logical_rating = st.slider(
    "Logical Quotient Rating",
    min_value=1,
    max_value=10,
    value=5
)

hackathons = st.slider(
    "Number of Hackathons",
    min_value=0,
    max_value=10,
    value=3
)

coding_rating = st.slider(
    "Coding Skills Rating",
    min_value=1,
    max_value=10,
    value=5
)

public_speaking = st.slider(
    "Public Speaking Points",
    min_value=1,
    max_value=10,
    value=5
)
self_learning = st.selectbox(
    "Self Learning Capability",
    ["yes", "no"]
)

extra_courses = st.selectbox(
    "Extra Courses Done",
    ["yes", "no"]
)

reading_writing = st.selectbox(
    "Reading and Writing Skills",
    ["poor", "medium", "excellent"]
)

memory_score = st.selectbox(
    "Memory Capability Score",
    ["poor", "medium", "excellent"]
)
certification = st.selectbox(
    "Certification",
    [
        "information security",
        "shell programming",
        "r programming",
        "distro making",
        "machine learning",
        "full stack",
        "hadoop",
        "app development",
        "python"
    ]
)

workshop = st.selectbox(
    "Workshop",
    [
        "testing",
        "database security",
        "game development",
        "data science",
        "system designing",
        "hacking",
        "cloud computing",
        "web technologies"
    ]
)

subject = st.selectbox(
    "Interested Subject",
    [
        "programming",
        "Management",
        "data engineering",
        "networks",
        "Software Engineering",
        "cloud computing",
        "parallel computing",
        "IOT",
        "Computer Architecture",
        "hacking"
    ]
)

career_area = st.selectbox(
    "Interested Career Area",
    [
        "testing",
        "system developer",
        "Business process analyst",
        "security",
        "developer",
        "cloud computing"
    ]
)
company_type = st.selectbox(
    "Type of Company",
    [
        "BPA",
        "Cloud Services",
        "product development",
        "Testing and Maintainance Services",
        "SAaS services",
        "Web Services",
        "Finance",
        "Sales and Marketing",
        "Product based",
        "Service Based"
    ]
)

senior_input = st.selectbox(
    "Taken Inputs From Seniors or Elders",
    ["yes", "no"]
)

book_type = st.selectbox(
    "Interested Type of Books",
    [
        "Series",
        "Autobiographies",
        "Travel",
        "Guide",
        "Health",
        "Journals",
        "Anthology",
        "Dictionaries",
        "Prayer books",
        "Art"
    ]
)

management_technical = st.selectbox(
    "Management or Technical",
    ["Management", "Technical"]
)

worker_type = st.selectbox(
    "Hard Worker or Smart Worker",
    ["hard worker", "smart worker"]
)

teamwork = st.selectbox(
    "Worked in Teams Ever?",
    ["yes", "no"]
)

introvert = st.selectbox(
    "Introvert",
    ["yes", "no"]
)
if st.button("Predict Career"):

    input_data = pd.DataFrame({
        "Logical quotient rating": [logical_rating],
        "hackathons": [hackathons],
        "coding skills rating": [coding_rating],
        "public speaking points": [public_speaking],
        "self-learning capability?": [self_learning],
        "Extra-courses did": [extra_courses],
        "certifications": [certification],
        "workshops": [workshop],
        "reading and writing skills": [reading_writing],
        "memory capability score": [memory_score],
        "Interested subjects": [subject],
        "interested career area ": [career_area],
        "Type of company want to settle in?": [company_type],
        "Taken inputs from seniors or elders": [senior_input],
        "Interested Type of Books": [book_type],
        "Management or Technical": [management_technical],
        "hard/smart worker": [worker_type],
        "worked in teams ever?": [teamwork],
        "Introvert": [introvert]
    })

    prediction = model.predict(input_data)

    predicted_role = target_encoder.inverse_transform(prediction)

    st.success(f"Recommended Career: {predicted_role[0]}")

    course_dict = {
        "Software Engineer": [
            "Data Structures & Algorithms",
            "System Design",
            "Python Programming"
        ],
        "Web Developer": [
            "HTML",
            "CSS",
            "JavaScript"
        ]
    }

    if predicted_role[0] in course_dict:
        st.subheader("Recommended Courses")

        for course in course_dict[predicted_role[0]]:
            st.write("•", course)
