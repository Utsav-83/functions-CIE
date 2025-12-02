from student1 import Student_details
import pytest

def test_student_details():
    expected_output = (
        "Student ID: 105\n"
        "Student Name: Naman\n"
        "Course Enrolled: BCA\n"
        "Academic Year: 2026\n"
    )

    result = Student_details(105, "Naman", "BCA", "2026")

    assert result == expected_output
