class Student:
    def __init__(self, name, student_id, attendence):
        self.name = name
        self.student_id = student_id
        self.attendance = False

    def mark_attendance(self):
        self.attendance = True


class AttendanceBook:
    def __init__(self):
        self.students = []
        self.student_ids = set() 

    def add_student(self, name, student_id):
        if student_id in self.student_ids:
            print(f"이미 존재하는 학번입니다: {student_id}")
            return
        student = Student(name, student_id)
        self.students.append(student)
        self.student_ids.add(student_id)
        print(f"학생 추가: {name}, 학번: {student_id}")

    def mark_student_attendance(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.mark_attendance()
                print(f"{student.name} 학생 출석 확인 완료.")
                return
        print(f"존재하지 않는 학번입니다: {student_id}")

    def get_attendance_summary(self):
        attendance_count = sum(1 for student in self.students if student.attendance)
        absence_count = len(self.students) - attendance_count
        return {"출석": attendance_count, "결석": absence_count}

    def get_student_list(self):
        
        return [student.name for student in self.students if student.attendance]

attendance_book = AttendanceBook()
attendance_book.add_student("황지원", "2024111537")
attendance_book.add_student("황정인", "2024111547")
attendance_book.add_student("김대은", "2020112429")

attendance_book.mark_student_attendance("2024111537")
attendance_book.mark_student_attendance("2024111547")

summary = attendance_book.get_attendance_summary()
print("출석 요약:", attendance_book.get_attendance_summary)

attended_students = attendance_book.get_student_list()
print("출석한 학생 목록:", attendance_book.get_student_list())
