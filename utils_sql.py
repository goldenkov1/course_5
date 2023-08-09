import csv

import psycopg2


class DBManager:

    def __init__(self):
        self.conn = None

    def conn_db(self):
        """Подключение к БД"""
        self.conn = psycopg2.connect(
            host='localhost',
            database='course_5',
            user='postgres',
            password='goldenslav1',
            port=5432
            )
        return self.conn

    def create_table(self):
        conn = self.conn_db()
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE employers(   
                employer_id INTEGER PRIMARY KEY,
                employer_name VARCHAR(255),
                employer_url VARCHAR(255),
                open_vacancy INTEGER
                )    
            """)

        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE vacancies(
                vacancy_id INTEGER PRIMARY KEY,
                area VARCHAR(255),
                name TEXT,
                employer_id INTEGER,
                employer VARCHAR(255),
                url_vacancy TEXT,
                salary_from INTEGER,
                salary_to INTEGER,
                currency VARCHAR(25)
                )
            """)
        cur.close()
        conn.commit()
        conn.close()

    def insert_emp(self):
        """
        Заполнение данными таблицы employers
        """
        file_employers = '/home/slava/PycharmProjects/course_5/employers.csv'
        conn = self.conn_db()
        try:
            with conn:
                with conn.cursor() as cur:
                    with open(file_employers) as csvfile:
                        readers = csv.DictReader(csvfile)
                        for reader in readers:
                            cur.execute("INSERT INTO employers VALUES (%s, %s, %s, %s)",
                                        (reader['emp_id'], reader['emp_name'], reader['emp_url'],
                                         reader['open_vacancy']))
        finally:
            conn.close()

    def insert_vac(self):
        """
        Заполнение данными таблицы vacancies
        """
        file_vacancies = '/home/slava/PycharmProjects/course_5/vacancies.csv'
        conn = self.conn_db()
        try:
            with conn:
                with conn.cursor() as cur:
                    with open(file_vacancies) as csvfile:
                        readers = csv.DictReader(csvfile)
                        for reader in readers:
                            cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                        (reader['vacancy_id'], reader['area'], reader['name'], reader['employer_id'],
                                         reader['employer'], reader['url'], reader['salary_from'], reader['salary_to'],
                                         reader['currency']))
        finally:
            conn.close()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        conn = self.conn_db()
        with conn.cursor() as cur:
            cur.execute("SELECT employer_name, open_vacancy FROM employers")
            rows = cur.fetchall()
            for row in rows:
                print(row)

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
            названия вакансии и зарплаты и ссылки на вакансию.
        """
        conn = self.conn_db()
        with conn.cursor() as cur:
            cur.execute("SELECT employer, name, salary_from, url_vacancy FROM vacancies")
            rows = cur.fetchall()
            for row in rows:
                print(row)

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        conn = self.conn_db()
        with conn.cursor() as cur:
            cur.execute("SELECT AVG(salary_from) FROM vacancies")
            rows = cur.fetchall()
            print(int(rows[0][0]))


    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
        pass
