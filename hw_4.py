class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_rate(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self):
        average_score = []
        for key, score in self.grades.items():
            average_score.append(sum(score)/len(score))
        return round(sum(average_score)/len(average_score), 1)

    def __ge__(self, student):
        return (self.average_score() >= student.average_score())

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_score()}\n"
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
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def average_score(self):
        average_score = []
        for key, score in self.lecturer_grades.items():
            average_score.append(sum(score)/len(score))
        return round(sum(average_score)/len(average_score), 1)

    def __ge__(self, lecturer):
        return (self.average_score() >= lecturer.average_score())

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_score()}")


student_1 = Student('Emma', 'Watson', 'w')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Jim', 'Kerry', 'w')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

best_lecturer = Lecturer('Tom', 'Stevenson')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Git']

best_reviewer = Reviewer('Kevin', 'Mitnick')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Git']
best_reviewer.rate_hw(student_1, 'Python', 10)
best_reviewer.rate_hw(student_1, 'Python', 5)
best_reviewer.rate_hw(student_1, 'Python', 10)
best_reviewer.rate_hw(student_1, 'Git', 10)
best_reviewer.rate_hw(student_1, 'Git', 5)
best_reviewer.rate_hw(student_1, 'Git', 5)

best_reviewer.rate_hw(student_2, 'Python', 10)
best_reviewer.rate_hw(student_2, 'Python', 5)
best_reviewer.rate_hw(student_2, 'Python', 10)
best_reviewer.rate_hw(student_2, 'Git', 10)
best_reviewer.rate_hw(student_2, 'Git', 10)
best_reviewer.rate_hw(student_2, 'Git', 10)

student_1.lecturer_rate(best_lecturer, "Python", 8)
student_1.lecturer_rate(best_lecturer, "Python", 9)
student_1.lecturer_rate(best_lecturer, "Python", 10)
student_1.lecturer_rate(best_lecturer, "Git", 10)
student_1.lecturer_rate(best_lecturer, "Git", 9)
student_1.lecturer_rate(best_lecturer, "Git", 10)

print(best_reviewer)
print(student_1)
print(student_1.grades)
print(student_2)
print(student_2.grades)
print(best_lecturer)
print(best_lecturer.lecturer_grades)
print(student_1 <= student_2)
