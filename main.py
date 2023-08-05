from pprint import pprint
employer_id = ['856498', '3591220', '5674346', '1993194', '9417901', '5674346', '2389722', '1535743', '2590583',
               '2509056']


from sql_manager import HH


def main():
    hh = HH("https://api.hh.ru/vacancies")
    pprint(hh.filtered_id())



if __name__ == "__main__":
    main()