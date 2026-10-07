import streamlit as st
from datetime import date

from planner import generate_study_plan
from progress import create_checklist, get_progress_summary


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Smart Study Planner",
    page_icon="📚",
    layout="wide"
)


# -----------------------------
# Custom styling
# -----------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    .hero {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        padding: 30px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
    }

    .hero h1 {
        margin-bottom: 8px;
        font-size: 38px;
    }

    .hero p {
        font-size: 17px;
        margin-bottom: 0;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .day-card {
        background-color: #111827;
        border: 1px solid #374151;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 18px;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
    }

    .day-title {
        font-size: 21px;
        font-weight: 700;
        color: white;
        margin-bottom: 12px;
    }

    .task-card {
        background-color: #1f2937;
        border-left: 5px solid #6366f1;
        color: white;
        padding: 12px 15px;
        border-radius: 8px;
        margin: 8px 0;
        font-size: 16px;
    }

    .summary-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 14px;
        padding: 18px;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    """
    <div class="hero">
        <h1>📚 Smart Study Planner</h1>
        <p>
            Create a personalized study timetable based on your subjects,
            exam dates, and available study hours.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Study settings
# -----------------------------

st.markdown(
    '<div class="section-title">⚙️ Study Settings</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    daily_hours = st.number_input(
        "Available study hours per day",
        min_value=1,
        max_value=12,
        value=4
    )

with col2:
    number_of_subjects = st.number_input(
        "Number of subjects",
        min_value=1,
        max_value=10,
        value=3
    )


# -----------------------------
# Subject input
# -----------------------------

st.markdown(
    '<div class="section-title">📖 Enter Your Subjects</div>',
    unsafe_allow_html=True
)

subjects = []

for i in range(int(number_of_subjects)):

    col1, col2 = st.columns([2, 1])

    with col1:
        subject_name = st.text_input(
            f"Subject {i + 1}",
            key=f"subject_{i}"
        )

    with col2:
        exam_date = st.date_input(
            f"Exam Date {i + 1}",
            min_value=date.today(),
            key=f"exam_date_{i}"
        )

    if subject_name:
        subjects.append(
            {
                "name": subject_name,
                "exam_date": exam_date
            }
        )


# -----------------------------
# Generate study plan
# -----------------------------

if st.button(
    "🚀 Generate Study Plan",
    use_container_width=True
):

    if not subjects:

        st.warning(
            "Please enter at least one subject."
        )

    else:

        plan = generate_study_plan(
            subjects,
            daily_hours
        )

        # Save plan
        st.session_state.plan = plan

        # Create checklist
        all_tasks = []

        for day in plan:

            for task in day["tasks"]:

                all_tasks.append(
                    f"{day['date']} - "
                    f"{task['subject']} "
                    f"({task['hours']} hour(s))"
                )

        st.session_state.checklist = create_checklist(
            all_tasks
        )


# -----------------------------
# Display study plan
# -----------------------------

if "plan" in st.session_state:

    plan = st.session_state.plan

    st.markdown(
        '<div class="section-title">📅 Your Study Plan</div>',
        unsafe_allow_html=True
    )

    for day in plan:

        # Day card
        st.markdown(
            f'<div class="day-card">'
            f'<div class="day-title">'
            f'📅 {day["date"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        # Tasks
        for task in day["tasks"]:

            st.markdown(
                f'<div class="task-card">'
                f'📘 <b>{task["subject"]}</b>'
                f'&nbsp;&nbsp; | &nbsp;&nbsp;'
                f'⏱️ {task["hours"]} hour(s)'
                f'</div>',
                unsafe_allow_html=True
            )

        # Close day card
        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# -----------------------------
# Progress checklist
# -----------------------------

if "checklist" in st.session_state:

    checklist = st.session_state.checklist

    st.markdown(
        '<div class="section-title">✅ Progress Checklist</div>',
        unsafe_allow_html=True
    )

    for i, item in enumerate(checklist):

        checklist[i]["completed"] = st.checkbox(
            item["task"],
            value=item["completed"],
            key=f"task_{i}"
        )


    # -----------------------------
    # Calculate progress
    # -----------------------------

    summary = get_progress_summary(
        checklist
    )


    # -----------------------------
    # Progress summary
    # -----------------------------

    st.markdown(
        '<div class="section-title">📊 Your Progress</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📚 Subjects",
            len(subjects)
        )

    with col2:

        st.metric(
            "⏱️ Daily Hours",
            daily_hours
        )

    with col3:

        st.metric(
            "📝 Completed Tasks",
            f"{summary['completed']} / {summary['total']}"
        )


    # Progress bar
    st.progress(
        summary["percentage"] / 100
    )

    st.write(
        f"### {summary['percentage']:.0f}% Completed"
    )