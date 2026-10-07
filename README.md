Smart Study Planner
1. Project Title

Smart Study Planner

A web-based application that helps students create a personalized study timetable based on their subjects, exam dates, and available study hours per day.

2. Problem Statement

Students often have multiple subjects with different exam dates and limited study time. Planning a proper revision schedule manually can be difficult and time-consuming.

Without a structured timetable, students may:

Spend too much time on one subject.
Ignore subjects with closer exams.
Have difficulty managing their available study hours.
Lose track of completed revision tasks.

Therefore, a simple system is needed to generate an organized study plan and help students track their revision progress.

3. Objective

The main objectives of the Smart Study Planner are:

To generate a personalized day-by-day study timetable.
To consider the exam dates of different subjects.
To prioritize subjects based on upcoming exams.
To use the student's available study hours efficiently.
To provide a checklist for completed study tasks.
To display the student's overall study progress.
4. Proposed Solution

The Smart Study Planner is a Streamlit-based web application.

The student provides:

Number of subjects.
Subject names.
Exam dates.
Available study hours per day.

The application processes this information and generates a day-by-day study timetable.

Subjects with nearer exam dates receive higher priority. The generated tasks can then be marked as completed using the progress checklist.

Basic flow:

Student Input → Plan Generation → Daily Study Tasks → Progress Tracking

5. Key Features
Dynamic Subject Input
Students can select the number of subjects they want to include in the planner.
Exam Date Input
Each subject can have its own exam date.
Daily Study Hours
Students can specify the number of hours they can study each day.
Automatic Study Plan Generation
The system creates a day-by-day timetable automatically.
Exam-Based Prioritization
Subjects with nearer exams are given higher priority.
Progress Checklist
Students can mark individual study tasks as completed.
Progress Percentage
The application calculates and displays the percentage of completed tasks.
Visual Study Plan
The timetable is displayed using organized cards for better readability.
6. How the System Works

The application works through the following steps:

The student enters the available study hours per day.
The student selects the required number of subjects.
The student enters each subject name and exam date.
The system identifies the upcoming exam dates.
Subjects are ordered according to their exam dates.
Study hours are allocated to the subjects based on their priority.
A day-by-day study timetable is generated.
The generated tasks are converted into a progress checklist.
Students mark tasks as completed.
The system calculates and displays the overall progress.
7. Technology Stack
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
Datetime	Date and exam-date calculations
Git	Version control
GitHub	Code sharing and team collaboration
ChatGPT	AI-assisted development

The project uses Python with Streamlit, as suggested for the Smart Study Planner problem.

8. Project Structure
SmartStudyPlanner/
│
├── app.py
├── planner.py
├── progress.py
├── requirements.txt
├── README.md
├── tests/
│
└── .gitignore
File Description

app.py
Contains the Streamlit user interface and connects the planner and progress modules.

planner.py
Contains the logic for generating the study timetable based on subjects, exam dates, and available study hours.

progress.py
Contains the checklist and progress calculation functions.

tests/
Contains testing files for checking the functionality of the project.

requirements.txt
Contains the Python libraries required to run the application.

README.md
Contains project documentation.

.gitignore
Prevents unnecessary local files such as the Python virtual environment from being uploaded to GitHub.

9. Algorithm / Planning Logic

The study planner follows a simple priority-based approach.

Steps
Get the current date.
Remove subjects whose exam dates have already passed.
Find the latest upcoming exam date.
Process each day until the last exam date.
Identify subjects whose exams have not yet occurred.
Sort these subjects according to their exam dates.
Give higher priority to subjects with nearer exams.
Allocate the available daily study hours.
Create study tasks for the day.
Repeat the process for the next day.

This produces a structured timetable while considering the student's available study time.

10. Progress Tracking

The application provides a checklist for all generated study tasks.

Each task initially starts as incomplete.

When the student completes a task, it can be marked using the checkbox.

The system then calculates:

Progress Percentage = (Completed Tasks / Total Tasks) × 100

The progress is displayed using:

A progress bar.
Completed task count.
Total task count.
Completion percentage.
11. Testing

The application was tested using different inputs to verify its functionality.

Tests performed
Tested with a single subject.
Tested with multiple subjects.
Tested with different numbers of subjects.
Tested with different available study hours.
Tested with different exam dates.
Tested with no subject entered.
Tested study-plan generation.
Tested progress checklist functionality.
Tested completion percentage calculation.
Tested whether the study plan remains visible after checking tasks.

The tests helped verify that the core study planning and progress tracking functionality works correctly.

12. Challenges Faced

During development, the team faced several challenges:

Designing a study-plan algorithm that considers exam dates.
Allocating study hours without exceeding the student's daily availability.
Creating a dynamic subject input interface.
Maintaining the generated study plan when Streamlit reruns the application.
Maintaining checklist states during interaction.
Integrating different modules developed by different team members.
Managing code using GitHub during team collaboration.
Designing a clean and user-friendly interface within the limited hackathon time.
13. AI Tool Usage

ChatGPT was used as an AI-assisted development tool during the project.

It helped the team with:

Understanding implementation approaches.
Planning the application structure.
Generating and improving code.
Debugging programming issues.
Streamlit integration.
Improving the user interface.
Understanding errors encountered during development.

The team was responsible for deciding the application requirements, integrating the code, testing the functionality, and verifying the final implementation.

14. Future Scope

The project can be further improved with:

Automatic rescheduling of missed study tasks.
Study reminders and notifications.
AI-based personalized study recommendations.
Performance analytics for individual subjects.
Difficulty-based study prioritization.
Mobile application support.
Cloud-based storage for saving student study plans.
Calendar integration for exam and study schedules.
15. Team Contribution
Rajesh
Developed the study-planning logic.
Worked on the Streamlit application.
Integrated the study planner with the user interface.
Worked on UI improvements and testing.
Nagendra
Developed the progress checklist and progress calculation functionality.
Worked on integration of progress tracking with the application.
Manoja
Worked on testing and validation.
Prepared presentation and supporting documentation.
Team
Discussed the problem and solution.
Integrated the modules.
Tested the complete application.
Prepared the final project and presentation.
16. How to Run the Project
Step 1: Clone the repository
git clone https://github.com/Rajesh-csit/SmartStudyPlanner.git
Step 2: Open the project folder
cd SmartStudyPlanner
Step 3: Install the required libraries
pip install -r requirements.txt
Step 4: Run the Streamlit application
python -m streamlit run app.py
Step 5: Open the application

Streamlit will provide a local URL such as:

http://localhost:8501

Open the URL in a web browser to use the Smart Study Planner.

Project Summary

Smart Study Planner provides students with a simple way to organize their exam preparation. By considering subjects, exam dates, and available study hours, the application generates a structured study timetable and provides progress tracking through an interactive checklist.

The project demonstrates the practical use of Python, Streamlit, date-based planning, basic algorithms, Git/GitHub collaboration, and AI-assisted development to solve a real student productivity problem.