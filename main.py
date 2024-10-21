from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from tqdm import tqdm
from time import sleep

if __name__ == '__main__':
    functions = [calculate_salary(), get_employees(), f"Текущая дата: {datetime.now()}"]
    for steps in tqdm(functions, desc='Выполнение процесса'):
        print(steps)











