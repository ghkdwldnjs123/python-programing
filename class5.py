class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = [] 

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0


class GradeBook:
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

    def add_student_score(self, student_id, score):
        for student in self.students:
            if student.student_id == student_id:
                student.add_score(score)
                print(f"{student.name} 학생에게 점수 추가: {score}")
                return
        print(f"존재하지 않는 학번입니다: {student_id}")

    def get_top_students(self, n):
        sorted_students = sorted(self.students, key=lambda s: s.calculate_average(), reverse=True)
        return [(student.name, student.calculate_average()) for student in sorted_students[:n]]

grade_book = GradeBook()
grade_book.add_student("황지원", "2024111537")
grade_book.add_student("황정인", "2024111547")
grade_book.add_student("김대은", "2020112429")

grade_book.add_student_score("2024111537", 100)
grade_book.add_student_score("2024111537", 90)
grade_book.add_student_score("2024111547", 1)
grade_book.add_student_score("2024111547", 5)
grade_book.add_student_score("2020112429", 0)
grade_book.add_student_score("2020112429", 2)

top_students = grade_book.get_top_students(2)
print("상위 2명의 학생:")
for name, avg_score in top_students:
    print(f"이름: {name}, 평균 점수: {avg_score:.2f}")
