class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg(self):
        grades_student = 0
        numb_grades = 0
        for numb in self.grades.values():
            grades_student += sum(numb)
            numb_grades += len(numb)
        res = round(grades_student / numb_grades, 1)
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнивается не со студентом')
            return
        if Student.avg(self) < Student.avg(other):
            return f'\nЛучший студент \n{other}'
        else:
            return f'\nЛучший студент \n{self}'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        res2 = Student.avg(self)
        res3 = ', '.join(self.courses_in_progress)
        res4 = ', '.join(self.finished_courses)
        return f'\n{res} \nСредняя оценка за домашние задания {str(res2)} \nКурсы в процессе изучения: {res3} \nЗавершенные курсы: {res4}'

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка с выставлением оценки лектору')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avgl(self):
        lecturer_student = 0
        numb_grades = 0
        for numb in self.grades.values():
            lecturer_student += sum(numb)
            numb_grades += len(numb)
        res = round(lecturer_student / numb_grades, 1)
        return res

    def __str__(self):
        res = f'\nИмя: {self.name}\nФамилия: {self.surname}'
        res2 = Lecturer.avgl(self)
        return f'{res} \nСредняя оценка за лекции: {res2}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return print(f'\nСравнивается не c лектором')
        if Lecturer.avgl(self) < Lecturer.avgl(other):
            return f'\nЛучший лектор \n{other}'
        else:
            return f'\nЛучший лектор \n{self}'


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
            return print('Ошибка с выставлением оценки студенту')

    def __str__(self):
        res = f'\nИмя: {self.name}\nФамилия: {self.surname}'
        return res


def avgr_stud(student, course):
    res = 0
    grade = 0
    numb = 0
    for stud in student:
        grade += sum(stud.grades[course])
        numb += len(stud.grades[course])
    res = grade / numb
    return f'\nСредняя оценка {round(res, 1)} у студентов за курс {course}'


def avgr_lect(lecturer, course):
    res = 0
    grade = 0
    numb = 0
    for lect in lecturer:
        grade += sum(lect.grades[course])
        numb += len(lect.grades[course])
    res = grade / numb
    return f'\nСредняя оценка {round(res, 1)} у лекторов за курс {course}'


pavel_student = Student('Павел', 'Леснов', 'мужской')
pavel_student.finished_courses += ['Git', 'Введение в программирование']
pavel_student.courses_in_progress += ['Python']
pavel_student.grades['Git'] = [10, 9, 8, 10, 9]
pavel_student.grades['Python'] = [10, 9]

mariya_student = Student('Мария', 'Зайцева', 'женский')
mariya_student.finished_courses += ['Git', 'Введение в программирование']
mariya_student.courses_in_progress += ['Python']
mariya_student.grades['Git'] = [10, 8]
mariya_student.grades['Python'] = [10, 9, 9, 8, 10]

gena_lecturer = Lecturer('Геннадий', 'Филимонов')
gena_lecturer.grades['Python'] = [10, 8]

galina_lecturer = Lecturer('Галина', 'Русских')
galina_lecturer.grades['Python'] = [10, 9]

ivan_reviewer = Reviewer('Иван', 'Шустов')
ivan_reviewer.courses_attached += ['Git']
valya_reviewer = Reviewer('Валентина', 'Медведева')
valya_reviewer.courses_attached += ['Python']

Student.rate_hw(mariya_student, galina_lecturer, 'Python', 10)
Reviewer.rate_hw(ivan_reviewer, mariya_student, 'Python', 10)

print('Рецензенты:')
print(ivan_reviewer)
print(valya_reviewer)
print('\nЛекторы:')
print(gena_lecturer)
print(galina_lecturer)
print('\nСтуденты:')
print(pavel_student)
print(mariya_student)

print(mariya_student < pavel_student)
print(galina_lecturer > gena_lecturer)

student_list = {pavel_student, mariya_student}
print(avgr_stud(student_list, 'Git'))

lecturer_list = {gena_lecturer, galina_lecturer}
print(avgr_lect(lecturer_list, 'Python'))