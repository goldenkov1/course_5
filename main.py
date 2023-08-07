from pprint import pprint

from api_hh import HH


def main():
    pprint(HH().get_employers())
    #pprint(HH.get_vacancies())



if __name__ == "__main__":
    main()