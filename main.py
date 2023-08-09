from pprint import pprint
from dotenv import load_dotenv
from utils_sql import DBManager
from api_hh import HH


def main():
    #pprint(HH().get_employers())
    #pprint(HH().get_vacancies())
    #DBManager().conn_db()
    #DBManager().insert_emp()
    #DBManager().create_table()
    #DBManager().get_companies_and_vacancies_count()
    # DBManager().get_all_vacancies()
    DBManager().get_avg_salary()



if __name__ == "__main__":
    main()