def create_checklist(tasks):
    """
    Create a checklist for the given study tasks.
    Each task starts as incomplete.
    """
    checklist = []

    for task in tasks:
        checklist.append({
            "task": task,
            "completed": False
        })

    return checklist


def calculate_progress(checklist):
    """
    Calculate the percentage of completed tasks.
    """
    if not checklist:
        return 0

    completed_tasks = sum(
        1 for item in checklist
        if item["completed"]
    )

    total_tasks = len(checklist)

    progress = (completed_tasks / total_tasks) * 100

    return progress


def get_progress_summary(checklist):
    """
    Return completed tasks, total tasks, and progress percentage.
    """
    total_tasks = len(checklist)

    completed_tasks = sum(
        1 for item in checklist
        if item["completed"]
    )

    progress = calculate_progress(checklist)

    return {
        "completed": completed_tasks,
        "total": total_tasks,
        "percentage": progress
    }