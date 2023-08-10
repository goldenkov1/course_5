from utils_sql import DBManager
from api_hh import HH


def main():
    HH().get_employers()
    HH().get_vacancies()
    DBManager().create_table()
    DBManager().insert_emp()
    DBManager().insert_vac()
    while True:
        request_vacancy = input("""
                                Введите соответствующую цифру
                                1 - список всех компаний и количество вакансий у каждой компании
                                2 -  список всех вакансий с указанием названия компании
                                   названия вакансии и зарплаты и ссылки на вакансию
                                3 - среднюю зарплату по вакансиям
                                4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям
                                5 - список всех вакансий, в названии которых содержится слово 'python'
                                0 - выход\n"""
                                )
        if request_vacancy == '1':
            DBManager().get_companies_and_vacancies_count()
        if request_vacancy == '2':
            DBManager().get_all_vacancies()
        if request_vacancy == '3':
            DBManager().get_avg_salary()
        if request_vacancy == '4':
            DBManager().get_vacancies_with_higher_salary()
        if request_vacancy == '5':
            DBManager().get_vacancies_with_keyword()
        if request_vacancy == '0':
            break


if __name__ == "__main__":
    main()