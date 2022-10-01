from pprint import pprint
import csv
import re

positions = 'lastname,firstname,surname,organization,position,phone,email'

with open("phonebook_raw.csv", encoding="utf-8") as file:
    rows = csv.reader(file, delimiter=",")
    contact_list = list(rows)
# pprint(contact_list)

"""поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. 
В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;"""

lastname_list = []
firstname_list = []
surname_list = []
email_list = []
position_list = []
org_list = []
phone_list = []


def find_lastname(contact_list):
    pattern = '[а-яёА-ЯЁ]*'
    for names in contact_list:
        if names[0] == 'lastname':
            pass
        else:
            result = re.match(pattern, names[0])
            lastname_list.append(result.group(0))


def find_firstname(contact_list):
    pattern = '[а-яёА-ЯЁ]*'
    pattern_2 = r'[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*'
    pattern_3 = r'[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*'
    for names in contact_list:
        result = re.search(pattern_2, names[0])
        result_2 = re.match(pattern, names[1])
        result_3 = re.search(pattern_3, names[0])
        if names[1] == 'firstname':
            pass
        elif result is not None:
            firstname_list.append(result.group(0).split(" ")[1])
        elif result_3:
            firstname_list.append(result_3.group(0).split(" ")[1])
        else:
            firstname_list.append(result_2.group(0))


def find_surname(contact_list):
    pattern = '[а-яёА-ЯЁ]*'
    pattern_2 = r'[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*'
    pattern_3 = r'[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*'
    for names in contact_list:
        result = re.search(pattern_2, names[0])
        result_2 = re.match(pattern_3, names[1])
        result_3 = re.search(pattern, names[2])
        if names[2] == 'surname':
            pass
        elif result is not None:
            surname_list.append(result.group(0).split(" ")[2])
        elif result_2 is not None:
            surname_list.append(result_2.group(0).split(" ")[1])
        else:
            surname_list.append(result_3.group(0))

"""
Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999
"""


def get_phones(contact_list):
    pattern = r'(\+7|8)+\s?\(?(\d{3})\)?\D?(\d{3})\D?(\d{2})\D?(\d{2})\s?\(?(доб.)?\s?(\d*)'
    for phone in contact_list:
        result = re.search(pattern, phone[5])
        if phone[5] == "phone":
            continue
        elif result is None:
            phone_list.append("")
        elif result.group(6) is not None:
            phone_list.append(
                f'+7({result.group(2)}){result.group(3)}-{result.group(4)}-{result.group(5)} доб.{result.group(7)}')
        else:
            phone_list.append(f'+7({result.group(2)}){result.group(3)}-{result.group(4)}-{result.group(5)}')


def get_org(contact_list):
    pattern = '.*'
    for org in contact_list:
        result = re.search(pattern, org[3])
        if org[3] == 'organization':
            continue
        elif result is None:
            org_list.append("")
        else:
            org_list.append(result.group(0))


def get_position(contact_list):
    pattern = '.*'
    for pos in contact_list:
        result = re.search(pattern, pos[4])
        if pos[4] == 'position':
            continue
        elif result is None:
            position_list.append("")
        else:
            position_list.append(result.group(0))


def get_email(contact_list):
    pattern = '.*'
    for mail in contact_list:
        result = re.search(pattern, mail[6])
        if mail[6] == 'email':
            continue
        elif result is None:
            email_list.append("")
        else:
            email_list.append(result.group(0))


find_lastname(contact_list)
find_firstname(contact_list)
find_surname(contact_list)
get_phones(contact_list)
get_org(contact_list)
get_position(contact_list)
get_email(contact_list)

new_list = [['lastname','firstname','surname','organization','position','phone','email']]

for i in range(0, len(lastname_list)):
    new_list.append([lastname_list[i], firstname_list[i], surname_list[i], org_list[i], position_list[i], phone_list[i],
                     email_list[i]])

pprint(new_list)