# Smart Study Planner
# Generates a day-by-day study timetable

from datetime import date, timedelta


def generate_study_plan(subjects, daily_hours):
    """
    Generate a simple day-by-day study timetable.

    subjects format:
    [
        {"name": "DSA", "exam_date": date(2026, 10, 10)},
        {"name": "DBMS", "exam_date": date(2026, 10, 13)}
    ]
    """

    if not subjects or daily_hours <= 0:
        return []

    today = date.today()

    # Remove subjects whose exam is already over
    subjects = [
        subject for subject in subjects
        if subject["exam_date"] >= today
    ]

    if not subjects:
        return []

    last_exam = max(subject["exam_date"] for subject in subjects)

    plan = []
    current_day = today

    while current_day <= last_exam:
        remaining_subjects = [
            subject for subject in subjects
            if subject["exam_date"] >= current_day
        ]

        if not remaining_subjects:
            break

        # Nearest exam gets highest priority
        remaining_subjects.sort(key=lambda subject: subject["exam_date"])

        hours_left = daily_hours
        tasks = []

        for subject in remaining_subjects:
            if hours_left <= 0:
                break

            days_left = (subject["exam_date"] - current_day).days

            # Give more time to subjects with nearer exams
            if days_left <= 2:
                hours = min(2, hours_left)
            else:
                hours = min(1, hours_left)

            tasks.append({
                "subject": subject["name"],
                "hours": hours
            })

            hours_left -= hours

        plan.append({
            "date": current_day,
            "tasks": tasks
        })

        current_day += timedelta(days=1)

    return plan
