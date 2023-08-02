import requests
import time
employer_id = ['856498', '3591220', '5674346', '1993194', '9417901', '5674346', '2389722', '1535743', '2590583',
                   '2509056']
class HH():
    """Класс для работы с АPI сайто hh.ru"""
    def __init__(self, url):
        self.url = url



    def request_api(self):
        """Получает JSON файл с вакансиями по AIP с сайта hh.ru"""
        all_hh_vacancies = []
        for page in range(10):
            time.sleep(1)
            params = {
                    "text": "python",
                    "page": page,
                    "per_page": "100"
            }
            all_hh_vacancies.extend(requests.get(self.url, params=params).json()["items"])
        return all_hh_vacancies

    def filtered_id(self):
        all_hh_vacancies = self.request_api()
        hh_vacancies = []
        for vacancy in all_hh_vacancies:
            if vacancy['employer']['id'] in employer_id:
                hh_vacancies.append(vacancy)
        return hh_vacancies


