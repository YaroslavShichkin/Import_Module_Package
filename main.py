import datetime
import time
DateCreation = datetime.datetime.today().strftime("%d.%M.%Y")
TimeCreation = time.strftime("%H:%M:%S")
print("Дата: ", DateCreation)
print("Время: ", TimeCreation, "\n")

print("Загрузка модуля salary.py...")
from salary import payroll_calculation
print("Модуль salary.py успешно загружен", "\n")


print("Загрузка модуля people.py...")
from people import employee_search
print("Модуль people.py успешно загружен", "\n")


print("Начало выполнения программы")
if __name__ == '__main__':
    payroll_calculation()
    employee_search()
print("Программа выполнена")