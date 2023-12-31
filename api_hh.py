import requests
import csv


class HH:
    """Класс для работы с АPI сайто hh.ru"""

    def __init__(self):
        self.employers_id= {
            "МДО": 736233,
            "ООО МосТрансАренда": 2753595,
            "Blue underlined link": 5269493,
            "ООО ЭС-АЙ Безопасность": 3471807,
            "ООО Телеформ ИС": 8178,
            "ООО Агент Умный полис": 936465,
            "РусЭкспресс": 1875694,
            "Avatec": 4937627,
            "KVINT": 4010751,
            "ООО Фабрика Решений": 4596113
        }

    def get_employers(self):
        """
               Метод класса HeadHunterAPI, для получения интересующих работодателй по их id.
               :return: employers_list
               """
        employers_list = []
        for i in self.employers_id.values():
            response = requests.get(f'https://api.hh.ru/employers/{i}').json()

            employers = {'emp_id': response['id'],
                         'emp_name': response['name'],
                         'emp_url': response['alternate_url'],
                         'open_vacancy': response['open_vacancies']}

            employers_list.append(employers)

        keys = employers_list[0].keys()
        with open("employers.csv", 'w', encoding='utf-8', newline='') as file:
            file_writer = csv.DictWriter(file, keys)
            file_writer.writeheader()
            file_writer.writerows(employers_list)

        return employers_list


    @staticmethod
    def get_vacancies():
        data = HH()
        data_hh = data.get_employers()

        emp_id = []
        for item in data_hh:
            emp_id.append(item['emp_id'])

        vac_emp = []
        for i in emp_id:
            vacancy = requests.get(f"https://api.hh.ru/vacancies?employer_id={i}").json()['items']

            for vacancy in vacancy:
                vacancy_id = vacancy['id']
                area = vacancy['area']['name']
                name = vacancy['name']
                employer_id = vacancy['employer']['id']
                employer = vacancy['employer']['name']
                url_vacancy = vacancy['alternate_url']
                salary = vacancy['salary']
                if not salary:
                    salary_from = 0
                    salary_to = 0
                    currency = 'Currency not specified'
                else:
                    salary_from = vacancy['salary']['from'] if vacancy['salary']['from'] else 0
                    salary_to = vacancy['salary']['to'] if vacancy['salary']['to'] else 0
                    currency = vacancy['salary']['currency'] if vacancy['salary'][
                        'currency'] else 'Currency not specified'

                vac_emp.append({'vacancy_id': vacancy_id,
                                'area': area,
                                'name': name,
                                'employer_id': employer_id,
                                'employer': employer,
                                'url': url_vacancy,
                                'salary_from': salary_from,
                                'salary_to': salary_to,
                                'currency': currency
                                })

        keys = vac_emp[0].keys()
        with open("vacancies.csv", 'w', encoding='utf-8', newline='') as file:
            file_writer = csv.DictWriter(file, keys)
            file_writer.writeheader()
            file_writer.writerows(vac_emp)

        return vac_emp

