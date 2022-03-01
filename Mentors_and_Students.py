class Student:
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached == self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
     
    def avr_grade(self, student):
        data = list(self.grades.values())
        list_grades = sum(data, [])
        sum_grades= sum(list_grades)
        if len(list_grades) != 0:
            self.average_grade += sum_grades/len(list_grades)
        else: 
            self.average_grade
    
    def __lt__(self, somebody):
        if not isinstance(somebody, Student):
            print("Такого студента нет")
            return
        return self.average_grade < somebody.average_grade
    
            
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_grade = 0

    def avr_grade(self, some_lecturer):

        data = self.grades.values()
        list_grades = sum(data, [])
        sum_grades = sum(list_grades)
        if len(list_grades) != 0:
            self.average_grade += (sum_grades / len(list_grades))
        else: 
            self.average_grade
    def __str__(self):
        return super().__str__() + f'\nСредняя оценка: {self.average_grade}'
    
    def __lt__(self, somebody):
        if not isinstance(somebody, Lecturer):
            print("Такого преподавателя нет")
            return
        return self.average_grade < somebody.average_grade


class Reviewer(Mentor):
    def __str__(self):
        return super().__str__()

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
cool_lecturer = Lecturer('Просто', 'Лектор')
victor_reviewer = Reviewer('Victor', 'Shmictor')
supercool_lecturer = Lecturer('Лучший', 'Лектор')
cool_reviewer = Reviewer('Some', 'Buddy')
riabov_student = Student('Evgenii', 'Riabov', 'male')



best_student.finished_courses +=['SQL']
best_student.courses_in_progress += ['Python', 'Java']
riabov_student.courses_in_progress += ['Python', 'Java']
riabov_student.finished_courses +=['SQL']

cool_lecturer.courses_attached += ['Python', 'Java']
supercool_lecturer.courses_attached += ['Python', 'Java']



cool_reviewer.courses_attached += ['Python', 'Java']
victor_reviewer.courses_attached += ['Python', 'Java']



best_student.rate_lecturer(supercool_lecturer, 'Java', 10)
best_student.rate_lecturer(supercool_lecturer, 'Python', 4)
riabov_student.rate_lecturer(supercool_lecturer, 'Java', 10)
riabov_student.rate_lecturer(supercool_lecturer, 'Python', 7)




riabov_student.rate_lecturer(cool_lecturer, 'Python', 10)
riabov_student.rate_lecturer(cool_lecturer, 'Java', 3)
best_student.rate_lecturer(cool_lecturer, 'Java', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 5)


cool_reviewer.rate_hw(best_student, 'Java', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
victor_reviewer.rate_hw(riabov_student, 'Java', 10)
victor_reviewer.rate_hw(riabov_student, 'Python', 2)
victor_reviewer.rate_hw(riabov_student, 'Python', 2)

best_student.avr_grade(best_student)
cool_lecturer.avr_grade(cool_lecturer)
supercool_lecturer.avr_grade(supercool_lecturer)
riabov_student.avr_grade(riabov_student)

students = [best_student, riabov_student ]
lecturers = [cool_lecturer, supercool_lecturer]

def get_lecturers_course_avr_grade(course, lecturers_list):
    grades_sum = 0
    num_lecturer = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            num_lecturer += 1
            for i,v in lecturer.grades.items():
                if i == course:
                    a = sum(v) / len(v)
                    grades_sum += a
        else:
            "Нет такого студента"
    return f'Средняя оценка всех лекторов в рамках курса по {course} составляет: {grades_sum/num_lecturer}'

def get_studens_course_avr_grade(course, students_list):
    grades_sum = 0
    num_students = 0
    for student in students_list:
        if isinstance(student, Student) and course in student.finished_courses or course in student.courses_in_progress:
            num_students += 1
            for i,v in  student.grades.items():
                if i == course:
                    a = sum(v) / len(v)
                    grades_sum += a
        else:
            "Нет такого студента"
    return f'Средняя оценка всех студентов в рамках курса по {course} составляет: {grades_sum/num_students}'

