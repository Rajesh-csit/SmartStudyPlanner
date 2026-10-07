import streamlit as st
from datetime import date

from planner import generate_study_plan


st.title("Smart Study Planner")

st.write("Create a personalized study timetable based on your subjects and exam dates.")

# Daily available study hours
daily_hours = st.number_input(
    "Available study hours per day",
    min_value=1,
    max_value=12,
    value=4
)

st.subheader("Enter Your Subjects")

subjects = []

for i in range(3):
    subject_name = st.text_input(f"Subject {i + 1}")

    exam_date = st.date_input(
        f"Exam date for Subject {i + 1}",
        min_value=date.today()
    )

    if subject_name:
        subjects.append({
            "name": subject_name,
            "exam_date": exam_date
        })


if st.button("Generate Study Plan"):

    if not subjects:
        st.warning("Please enter at least one subject.")

    else:
        plan = generate_study_plan(subjects, daily_hours)

        st.subheader("Your Study Plan")

        for day in plan:
            st.write(f"### {day['date']}")

            for task in day["tasks"]:
                st.write(
                    f"- {task['subject']} → {task['hours']} hour(s)"
                )