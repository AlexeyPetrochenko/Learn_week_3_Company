from functools import wraps
# В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
# Ваши задачи такие:
# 1. Вывести названия всех отделов
# 2. Вывести имена всех сотрудников компании.
# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела


departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


# def get_full_name(employee: dict[str, str | int]) -> str:
#     first_name = employee['first_name']
#     last_name = employee['last_name']
#     return f'{first_name} {last_name}'


# Это просто что бы вспомнить декораторы)
def indent_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print()
        return result
    return inner


# 1. Вывести названия всех отделов
@indent_decorator
def print_title_departments(list_departments: list[dict[str,  str | list[dict[str, str | int]]]]) -> None:
    for department in list_departments:
        print(department['title'])


print_title_departments(departments)


# 2. Вывести имена всех сотрудников компании.

def get_all_employers(list_departments) -> list[dict[str, str | int]]:
    employers = []
    for department in list_departments:
        for employee in department['employers']:
            employers.append(employee)
    return employers


for employee in get_all_employers(departments):
    print(employee['first_name'])
print()


# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
def print_employers_and_departament(list_departament):
    for department in list_departament:
        name_departament = department['title']
        print(f'{name_departament}:')
        for employee in department['employers']:
            name = employee['first_name']
            print(name)
        print()


print_employers_and_departament(departments)


# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
@indent_decorator
def salary_statistics(list_employers: list[dict[str, str | int]], salary_comparison: int, operand: bool):
    for employee in list_employers:
        salary = employee['salary_rub']
        full_name = employee['first_name']
        if operand:
            if salary > salary_comparison:
                print(full_name)
        else:
            if salary < salary_comparison:
                print(full_name)


all_employers = get_all_employers(departments)
salary_statistics(all_employers, 100_000, True)

# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
salary_statistics(all_employers, 80_000, False)


# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
def department_expenses(list_departments):
    for department in list_departments:
        department_employers = department['employers']
        title_department = department['title']
        salary_all_employers = 0
        for employee in department_employers:
            salary_all_employers += employee['salary_rub']
        print(f'{title_department}: {salary_all_employers:,} руб.')


department_expenses(departments)





