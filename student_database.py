import json
import os

def set_student(data_list):
    """Записывает данные в словарь. Пример записи: {'Иван' :(['Иван', '1A'], {Инф:[5,5,5,5,4]})}"""
    student_db[data_list[0]] = data_list[1:], {}

def set_rating(last_name, lesson, rating):
    """Добавление оценок"""
    if student_db.get(last_name) is None:
        print(f'Ученик, с фамилией {last_name} не найден')
        print(student_db)
    else:
        if lesson in student_db[last_name][1]:
            student_db[last_name][1][lesson].extend(rating)
        else:
            student_db[last_name][1][lesson] = rating       


def get_student(Last_name_student):
    """Вывод данных ученика"""
    if student_db.get(Last_name_student) is None:
        print(f'Ученик, с фамилией {Last_name_student} не найден')
    else:
        data = student_db[Last_name_student]
        print(f'{Last_name_student} {",".join(data[0])}:')
        print(*[f'{key}:{",".join(value)}' for key, value in data[1].items()], sep='\n')

def save_db():
    """Сохраниние данных учеников из словаря ' student_db' в файл формата .json"""
    json.dump(student_db, open('db_student.json', 'w'))

def load_db():
    """Сохранить данные учеников из файла .json в словарь 'student_db' """
    global student_db
    if os.stat('db_student.json').st_size == 0:
        student_db = {}
    else:
        student_db = json.load(open('db_student.json'))


