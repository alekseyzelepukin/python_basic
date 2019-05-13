__author__ = 'Зелепукин Алексей Юрьевич'


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, school_name):
        self._school_name = school_name
        self._grades = []

    def get_school_name(self):
        return self._school_name

    def add_grades(self, grades):
        for grade in grades:
            if grade not in self._grades:
                self._grades.append(grade)

    def del_grades(self, grades):
        for grade in grades:
            if grade in self._grades:
                self._grades.remove(grade)

    def get_grades(self):
        return list(grade.get_grade_name() for grade in self._grades)

    def get_grade_students(self, grade_name):
        for grade in self._grades:
            if grade_name == grade.get_grade_name():
                return grade.get_students()

    def get_student_info(self, student_name):
        for grade in self._grades:
            for student in grade._students:
                if student_name == student.get_short_name():
                    return [student_name,
                            student.get_grade(),
                            list({teacher.get_short_name(): subject} for subject, teacher in grade._teachers.items())]

    def get_student_parents(self, student_name):
        for grade in self._grades:
            for student in grade._students:
                if student_name == student.get_short_name():
                    return student.get_parents()

    def get_grade_teachers(self, grade_name):
        for grade in self._grades:
            if grade_name == grade.get_grade_name():
                return grade.get_teachers()


class Grade:
    def __init__(self, grade_name):
        self._grade_name = grade_name
        self._students = []
        self._teachers = dict()

    def get_grade_name(self):
        return self._grade_name

    def add_students(self, students):
        for student in students:
            if student not in self._students:
                student.set_grade(self)
                self._students.append(student)

    def del_students(self, students):
        for student in students:
            if student in self._students:
                student.set_grade(None)
                self._students.remove(student)

    def get_students(self):
        return list(student.get_short_name() for student in self._students)

    def add_teachers(self, teachers):
        for teacher in teachers:
            if teacher not in self._teachers.items():
                teacher.add_grade(self._grade_name)
                self._teachers[teacher.get_subject()] = teacher

    def del_teachers(self, teachers):
        for teacher in teachers:
            if teacher in self._teachers.items():
                teacher.del_grade(self._grade_name)
                del self._teachers[teacher.get_subject()]

    def get_teachers(self):
        return list(teacher.get_short_name() for teacher in self._teachers.values())


class Person:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    def get_full_name(self):
        return f'{self._last_name} {self._first_name} {self._middle_name}'

    def get_short_name(self):
        return f'{self._last_name} {self._first_name[:1]}.{self._middle_name[:1]}.'


class Student(Person):
    def __init__(self, last_name, first_name, middle_name, father, mother):
        Person.__init__(self, last_name, first_name, middle_name)
        self._parents = [father, mother]
        self._grade = None

    def get_parents(self):
        return list(parent.get_short_name() for parent in self._parents)

    def set_grade(self, grade):
        self._grade = grade

    def get_grade(self):
        if self._grade is not None:
            return self._grade.get_grade_name()
        else:
            return None


class Teacher(Person):
    def __init__(self, last_name, first_name, middle_name, subject):
        Person.__init__(self, last_name, first_name, middle_name)
        self._subject = subject
        self._grades = []

    def get_subject(self):
        return self._subject

    def add_grade(self, grade_name):
        if grade_name not in self._grades:
            self._grades.append(grade_name)

    def del_grade(self, grade_name):
        if grade_name in self._grades:
            self._grades.remove(grade_name)

    def get_grades(self):
        return list(grade for grade in self._grades)


school = School('1408')

student1 = Student('Иванов', 'Иван', 'Иванович',
                   Person('Иванов', 'Иван', 'Андреевич'), Person('Иванова', 'Наталья', 'Сергеевна'))
student2 = Student('Сидоров', 'Сидор', 'Сидорович',
                   Person('Сидоров', 'Сидр', 'Владимирович'), Person('Сидорова', 'Дарья', 'Юрьевна'))
student3 = Student('Петров', 'Петр', 'Петрович',
                   Person('Петров', 'Петр', 'Станиславович'), Person('Петрова', 'Анна', 'Дмитриевна'))
student4 = Student('Дмитриев', 'Дмитрий', 'Дмитриевич',
                   Person('Дмитриев', 'Дмитрий', 'Анатольевич'), Person('Дмитриева', 'Жанна', 'Эдуардовна'))

teacher1 = Teacher('Рашка', 'Себастья', 'Себастьянович', 'Машинное обучение')
teacher2 = Teacher('Лутц', 'Марк', 'Маркович', 'Программирование')
teacher3 = Teacher('Кнут', 'Дональд', 'Дональдович', 'Алгоритмы')
teacher4 = Teacher('Розенблатт', 'Фрэнк', 'Фрэнкович', 'Искусственный интеллект')

grade1 = Grade('5A')
grade2 = Grade('6B')

grade1.add_students([student1, student2])
grade1.add_teachers([teacher1, teacher2, teacher4])
grade2.add_students([student3, student4])
grade2.add_teachers([teacher2, teacher3])

school.add_grades([grade1, grade2])

# 1. Получить полный список всех классов школы
print(school.get_grades())
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
print(school.get_grade_students('5A'))
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
print(school.get_student_info('Иванов И.И.'))
# 4. Узнать ФИО родителей указанного ученика
print(school.get_student_parents('Дмитриев Д.Д.'))
# 5. Получить список всех Учителей, преподающих в указанном классе
print(school.get_grade_teachers('6B'))
