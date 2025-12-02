def Student_details(Student_ID, Student_Name, Course_Enrolled, Academic_Year):
    result = (
        f"Student ID: {Student_ID}\n"
        f"Student Name: {Student_Name}\n"
        f"Course Enrolled: {Course_Enrolled}\n"
        f"Academic Year: {Academic_Year}\n"
    )
    return result


if __name__ == "__main__":
    print(Student_details(105, "Naman", "BCA", "2026"))
