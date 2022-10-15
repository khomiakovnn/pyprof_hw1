from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

def main():
    calculate_salary()
    get_employees()
    date = datetime.today().strftime("%A, %d %B %Y")
    print(date)


if __name__ == '__main__':
    main()
