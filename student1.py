
def student_details(Student_ID, Student_Name, Course_Enrolled, Academic_Year):
    result = (
        f"Student ID: {Student_ID}\n"
        f"Student Name: {Student_Name}\n"
        f"Course Enrolled: {Course_Enrolled}\n"
        f"Academic Year: {Academic_Year}\n"
    )
    return result

if __name__ == "__main__":
    Student_ID = 105
    Student_Name = "Naman"
    Course_Enrolled = "BCA"
    Academic_Year = "2026"
    
    print(student_details(Student_ID, Student_Name, Course_Enrolled, Academic_Year))

    
