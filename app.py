import streamlit as st
from datetime import date

from planner import generate_study_plan
from progress import create_checklist, get_progress_summary


st.title("Smart Study Planner")

st.write(
    "Create a personalized study timetable based on your subjects and exam dates."
)

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


# Generate study plan
if st.button("Generate Study Plan"):

    if not subjects:
        st.warning("Please enter at least one subject.")

    else:
        plan = generate_study_plan(subjects, daily_hours)

        # Save plan so it stays after checkbox clicks
        st.session_state.plan = plan

        # Create checklist from generated tasks
        all_tasks = []

        for day in plan:
            for task in day["tasks"]:
                all_tasks.append(
                    f"{day['date']} - {task['subject']} ({task['hours']} hour(s))"
                )

        # Save checklist
        st.session_state.checklist = create_checklist(all_tasks)


# Show study plan if it exists
if "plan" in st.session_state:

    plan = st.session_state.plan

    st.subheader("Your Study Plan")

    for day in plan:
        st.write(f"### {day['date']}")

        for task in day["tasks"]:
            st.write(
                f"- {task['subject']} → {task['hours']} hour(s)"
            )


# Show progress checklist if it exists
if "checklist" in st.session_state:

    checklist = st.session_state.checklist

    st.subheader("Progress Checklist")

    for i, item in enumerate(checklist):

        checklist[i]["completed"] = st.checkbox(
            item["task"],
            value=item["completed"],
            key=f"task_{i}"
        )


    # Calculate progress
    summary = get_progress_summary(checklist)

    st.subheader("Your Progress")

    st.progress(summary["percentage"] / 100)

    st.write(
        f"{summary['completed']} / {summary['total']} tasks completed"
    )

    st.write(
        f"Progress: {summary['percentage']:.0f}%"
    )