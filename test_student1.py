from student1 import Student_details
import pytest
def test_student_details():
    expected_output = (
        "Student ID: 105\n"
        "Student Name: Naman\n"
        "Course Enrolled: BCA\n"
        "Academic Year: 2026\n"
    )

    
    assert Student_details(Student_ID, Student_Name, Course_Enrolled, Academic_Year) == expected_output
