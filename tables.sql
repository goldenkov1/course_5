DROP TABLE employers
CREATE TABLE employers(
                employer_id INTEGER PRIMARY KEY,
                employer_name VARCHAR(255),
                employer_url VARCHAR(255),
                open_vacancy INTEGER
                );

 DROP TABLE vacancies
 CREATE TABLE vacancies(
                vacancy_id INTEGER PRIMARY KEY,
                area VARCHAR(255),
                name_vacancy TEXT,
                employer_id INTEGER,
                employer VARCHAR(255),
                url_vacancy TEXT,
                salary_from INTEGER,
                salary_to INTEGER,
                currency VARCHAR(25)
                );

INSERT INTO employers VALUES
(736233, 'МДО', 'https://hh.ru/employer/736233', 2),
(2753595, 'МосТрансАренда', 'https://hh.ru/employer/2753595', 6),
(5269493, 'Blue underlined link', 'https://hh.ru/employer/5269493', 2),
(3471807, 'ЭС-АЙ Безопасность', 'https://hh.ru/employer/3471807', 2),
(8178, 'Телеформ ИС', 'https://hh.ru/employer/8178', 2),
(936465, 'Агент Умный полис', 'https://hh.ru/employer/936465', 7),
(1875694, 'РусЭкспресс', 'https://hh.ru/employer/1875694', 8),
(4937627, 'Avatec', 'https://hh.ru/employer/4937627', 2),
(4010751, 'KVINT', 'https://hh.ru/employer/4010751', 5),
(4596113, 'Фабрика Решений', 'https://hh.ru/employer/4596113', 3);

INSERT INTO employers VALUES
(84302495, 'Москва', 'Стажер-разработчик Python (Удаленно) (Рейтинг на CodeForces - Важно!)', 736233, 'МДО', 'https://hh.ru/vacancy/84302495', 60000, 0, 'RUR'),
(84157394, 'Москва', 'Клиентский менеджер', 736233, 'МДО', 'https://hh.ru/vacancy/84157394', 160000, 0, 'RUR'),
(84631676, 'Москва', 'Разработчик Odoo (Python)', 2753595, 'МосТрансАренда', 'https://hh.ru/vacancy/84631676', 150000, 200000, 'RUR'),
(84678036, 'Москва', 'Кладовщик-снабженец', 2753595, 'МосТрансАренда', 'https://hh.ru/vacancy/84678036', 80000, 90000, 'RUR'),
(83770680, 'Москва', 'Менеджер по продажам', 2753595, 'МосТрансАренда', 'https://hh.ru/vacancy/83770680', 100000, 0, 'RUR'),
(83617644, 'Москва', 'Руководитель отдела продаж', 2753595, 'МосТрансАренда', 'https://hh.ru/vacancy/83617644', 150000, 250000, 'RUR'),
(83697654, 'Москва', 'Механик (выездной) по \u2062ремонту строительной спецтехники', 2753595, 'МосТрансАренда', 'https://hh.ru/vacancy/83697654', 110000, 140000, 'RUR'),
(83697092, 'Москва', 'Механик по ремонту строительной техники', 2753595, 'МосТрансАренда', 'https://hh.ru/vacancy/83697092', 70000, 80000, 'RUR'),
(84558768, 'Москва', 'Junior Python-разработчик', 5269493, 'Blue underlined link', 'https://hh.ru/vacancy/84558768', 110000, 140000, 'RUR'),
(84558094, 'Москва', 'Middle+ Python-разработчик', 5269493, 'Blue underlined link', 'https://hh.ru/vacancy/84558094', 230000, 270000, 'RUR'),
(84671395, 'Москва', 'Middle Python Developer', 3471807, 'ЭС-АЙ Безопасность', 'https://hh.ru/vacancy/84671395', 200000, 350000, 'RUR'),
(84511566, 'Москва', 'QA \\ Тестировщик', 3471807, 'ЭС-АЙ Безопасность', 'https://hh.ru/vacancy/84511566', 80000, 0, 'RUR'),
(83617001, 'Москва', 'Python Developer', 8178, 'Телеформ ИС', 'https://hh.ru/vacancy/83617001', 120000, 180000, 'RUR'),
(83807874, 'Москва', 'Системный администратор', 8178, 'Телеформ ИС', 'https://hh.ru/vacancy/83807874', 70000, 0, 'RUR'),
(84358318, 'Санкт-Петербург', 'Junior+ QA Engineer в IT-компании', 936465, 'Агент Умный полис', 'https://hh.ru/vacancy/84358318', 100000, 0, 'RUR'),
(84912889, 'Санкт-Петербург', 'Оператор call-центра (удаленно)', 936465, 'Агент Умный полис', 'https://hh.ru/vacancy/84912889', 45000, 70000, 'RUR'),
(83747049, 'Санкт-Петербург', 'Бизнес-ассистент', 936465, 'Агент Умный полис', 'https://hh.ru/vacancy/83747049', 70000, 90000, 'RUR'),
(84018264, 'Санкт-Петербург', 'Middle+ Python Developer (backend)', 936465, 'Агент Умный полис', 'https://hh.ru/vacancy/84018264', 250000, 300000, 'RUR'),
(84270967, 'Санкт-Петербург', 'Frontend developer (Angular)', 936465, 'Агент Умный полис', 'https://hh.ru/vacancy/84270967', 0, 0, 'Currency not specified'),
(84200508, 'Санкт-Петербург', 'Ведущий системный аналитик', 936465, 'Агент Умный полис', 'https://hh.ru/vacancy/84200508', 0, 300000, 'RUR'),
(83567321, 'Санкт-Петербург', 'Архитектор решений / Solution architect', 936465, 'Агент Умный полис', 'https://hh.ru/vacancy/83567321', 0, 0, 'Currency not specified'),
(84765957, 'Москва', 'Разработчик Python', 1875694, 'РусЭкспресс', 'https://hh.ru/vacancy/84765957', 70000, 100000, 'RUR'),
(83785812, 'Москва', 'Экономист-аналитик (удаленно)', 1875694, 'РусЭкспресс', 'https://hh.ru/vacancy/83785812', 50000, 80000, 'RUR'),
(83907794, 'Москва', 'Программист Python', 1875694, 'РусЭкспресс', 'https://hh.ru/vacancy/83907794', 80000, 120000, 'RUR'),
(83787205, 'Москва', 'Специалист по тендерам', 1875694, 'РусЭкспресс', 'https://hh.ru/vacancy/83787205', 50000, 0, 'RUR'),
(83515296, 'Москва', 'Специалист по работе с поставщиками', 1875694, 'РусЭкспресс', 'https://hh.ru/vacancy/83515296', 50000, 0, 'RUR'),
(83516623, 'Москва', 'Специалист по работе с клиентами', 1875694, 'РусЭкспресс', 'https://hh.ru/vacancy/83516623', 50000, 0, 'RUR'),
(83624979, 'Москва', 'Руководитель тендерного отдела', 1875694, 'РусЭкспресс', 'https://hh.ru/vacancy/83624979', 50000, 70000, 'RUR'),
(82503535, 'Москва', 'Руководитель отдела по работе с маркетплейсами', 1875694, 'РусЭкспресс', 'https://hh.ru/vacancy/82503535', 80000, 150000, 'RUR'),
(84448764, 'Москва', 'Python-разработчик', 4937627, 'Avatec', 'https://hh.ru/vacancy/84448764', 150000, 200000, 'RUR'),
(84132429, 'Москва', 'Технический писатель', 4937627, 'Avatec', 'https://hh.ru/vacancy/84132429', 100000, 200000, 'RUR'),
(84433047, 'Волгоград', 'Специалист отдела мониторинга голосовых роботов', 4010751, 'KVINT', 'https://hh.ru/vacancy/84433047', 36000, 43000, 'RUR'),
(84443445, 'Москва', 'Middle Системный администратор Linux (ubuntu)/Devops', 4010751, 'KVINT', 'https://hh.ru/vacancy/84443445', 180000, 280000, 'RUR'),
(83829617, 'Москва', 'Python Developer Middle (Backend), удаленно', 4010751, 'KVINT', 'https://hh.ru/vacancy/83829617', 160000, 240000, 'RUR'),
(83336798, 'Санкт-Петербург', 'Системный аналитик', 4010751, 'KVINT', 'https://hh.ru/vacancy/83336798', 130000, 180000, 'RUR'),
(83324797, 'Санкт-Петербург', 'Python Developer Middle (Backend)', 4010751, 'KVINT', 'https://hh.ru/vacancy/83324797', 0, 0, 'Currency not specified'),
(84835419, 'Москва', 'UI/UX Дизайнер', 4596113, 'Фабрика Решений', 'https://hh.ru/vacancy/84835419', 80000, 140000, 'RUR'),
(82929790, 'Москва', 'Разработчик Python (Django, DRF)', 4596113, 'Фабрика Решений', 'https://hh.ru/vacancy/82929790', 150000, 250000, 'RUR'),
(82396438, 'Москва', 'Менеджер проектов (IT)', 4596113, 'Фабрика Решений', 'https://hh.ru/vacancy/82396438', 0, 150000, 'RUR');

SELECT employer_name, open_vacancy FROM employers;

SELECT employer, name_vacancy, salary_from, url_vacancy FROM vacancies;

SELECT AVG(salary_from) FROM vacancies;

SELECT * FROM vacancies
WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies;

SELECT * FROM vacancies
WHERE name_vacancy LIKE '%Python%';