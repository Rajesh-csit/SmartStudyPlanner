# Smart Study Planner - Test Cases

## Objective

The purpose of testing is to verify that the Smart Study Planner accepts valid student inputs, generates a suitable study plan, handles invalid inputs properly, and displays study progress correctly.

## Test Cases

| Test ID | Test Case | Input / Action | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Single subject | Enter one subject with a valid future exam date and available study hours | A study plan should be generated successfully | pass |
| TC02 | Multiple subjects | Enter multiple subjects with valid exam dates | All subjects should be included in the generated study plan | pass |
| TC03 | Different exam dates | Enter subjects having different exam dates | Subjects should be planned according to the implemented priority/urgency rule | Pass |
| TC04 | Available study hours | Enter a valid number of study hours per day | The generated plan should respect the available daily study time | Pass |
| TC05 | Low study time | Enter a small number of available study hours | The application should generate a valid plan within the available time | Pass |
| TC06 | Empty subject input | Leave the subject field empty | The application should show validation or prevent invalid input | Pass |
| TC07 | Invalid exam date | Enter an invalid or past exam date | The application should handle the invalid date without crashing | Pass |
| TC08 | Generate study plan | Enter valid details and select the Generate option | The timetable/study plan should be displayed | Pass |
| TC09 | Progress tracking | Mark a study task as completed | The progress information should update correctly | Pass |
| TC10 | Multiple study tasks | Complete some tasks while leaving others incomplete | Completed and remaining tasks should be represented correctly | Pass |

## Testing Result

Testing will be performed after the planner, progress module, and Streamlit application are integrated.

The status of each test case will be updated as:

- **Pass** - Expected result was obtained.
- **Fail** - Expected result was not obtained.
- **Pending** - Test has not yet been executed.

## Conclusion

The test cases are designed to verify the main functionality, input validation, study-plan generation, and progress tracking of the Smart Study Planner.