class Student:
    students = {}

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.students[f"{self.name} {self.surname}"] = self.grades

    def lecturer_rate(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_mark(self):
        average_score = []
        for key, mark in self.grades.items():
            average_score.append(sum(mark)/len(mark))
        return round(sum(average_score)/len(average_score), 1)

    def __ge__(self, student):
        return (self.average_mark() >= student.average_mark())

    def __eq__(self, student):
        return (self.average_mark() == student.average_mark())

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_mark()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    lecturers = {}

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}
        self.lecturers[f"{self.name} {self.surname}"] = self.lecturer_grades

    def average_mark(self):
        average_mark = []
        for key, score in self.lecturer_grades.items():
            average_mark.append(sum(score)/len(score))
        return round(sum(average_mark)/len(average_mark), 1)

    def __ge__(self, lecturer):
        return (self.average_mark() >= lecturer.average_mark())

    def __eq__(self, lecturer):
        return (self.average_mark() == lecturer.average_mark())

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_mark()}")


def students_average_mark(students, cours):
    course_mark = []
    for student, courses_info in students.items():
        for cours_info, grades in courses_info.items():
            if cours == cours_info:
                course_mark.append(sum(grades)/len(grades))
    courses_average_mark = round(sum(course_mark)/len(course_mark), 1)
    return f"Средняя оценка за домашние задания по всем студентам по {cours}: {courses_average_mark}"


def lecturers_average_mark(lecturers, cours):
    course_mark = []
    for student, courses_info in lecturers.items():
        for cours_info, grades in courses_info.items():
            if cours == cours_info:
                course_mark.append(sum(grades)/len(grades))
    courses_average_mark = round(sum(course_mark)/len(course_mark), 1)
    return f"Средняя оценка за ведение лекций по всем лекторам по {cours}: {courses_average_mark}"

student_1 = Student('Emma', 'Watson', 'w')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Jim', 'Carrey', 'm')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

best_lecturer_1 = Lecturer('Tom', 'Stevenson')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_1.courses_attached += ['Git']

best_lecturer_2 = Lecturer('Eric', 'Spilsnerer')
best_lecturer_2.courses_attached += ['Python']
best_lecturer_2.courses_attached += ['Git']

best_reviewer = Reviewer('Kevin', 'Mitnick')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Git']
best_reviewer.rate_hw(student_1, 'Python', 1)
best_reviewer.rate_hw(student_1, 'Python', 2)
best_reviewer.rate_hw(student_1, 'Python', 3)
best_reviewer.rate_hw(student_1, 'Git', 4)
best_reviewer.rate_hw(student_1, 'Git', 5)
best_reviewer.rate_hw(student_1, 'Git', 6)

best_reviewer.rate_hw(student_2, 'Python', 7)
best_reviewer.rate_hw(student_2, 'Python', 8)
best_reviewer.rate_hw(student_2, 'Python', 9)
best_reviewer.rate_hw(student_2, 'Git', 10)
best_reviewer.rate_hw(student_2, 'Git', 9)
best_reviewer.rate_hw(student_2, 'Git', 9)

student_1.lecturer_rate(best_lecturer_1, "Python", 7)
student_1.lecturer_rate(best_lecturer_1, "Python", 7)
student_1.lecturer_rate(best_lecturer_1, "Python", 7)
student_2.lecturer_rate(best_lecturer_1, "Git", 8)
student_2.lecturer_rate(best_lecturer_1, "Git", 8)
student_2.lecturer_rate(best_lecturer_1, "Git", 8)

student_1.lecturer_rate(best_lecturer_2, "Python", 6)
student_1.lecturer_rate(best_lecturer_2, "Python", 6)
student_1.lecturer_rate(best_lecturer_2, "Python", 6)
student_2.lecturer_rate(best_lecturer_2, "Git", 9)
student_2.lecturer_rate(best_lecturer_2, "Git", 9)
student_2.lecturer_rate(best_lecturer_2, "Git", 9)

res = students_average_mark(Student.students, "Python")
print(best_reviewer)
print(student_1)
print(student_1.grades)
print(student_2)
print(student_2.grades)
print(best_lecturer_1)
print(best_lecturer_1.lecturer_grades)
print(best_lecturer_2)
print(best_lecturer_2.lecturer_grades)
print(student_1 <= student_2)
print(student_1 == student_2)
print(student_1 >= student_2)
print(students_average_mark(Student.students, "Git"))
print(students_average_mark(Student.students, "Python"))
print(lecturers_average_mark(Lecturer.lecturers, "Python"))
print(lecturers_average_mark(Lecturer.lecturers, "Git"))