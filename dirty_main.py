from application.salary import *
from application.db.people import *
from datetime import *

def main():
    calculate_salary()
    get_employees()
    date = datetime.today().strftime("%A, %d %B %Y")
    print(date)


if __name__ == '__main__':
    main()