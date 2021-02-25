from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
from func import create_result_list, result_sorting_the_file
from data import pattern, pattern_to_sub


with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

form_dict = result_sorting_the_file(pattern, contacts_list, pattern_to_sub)
reuslt_list = create_result_list(form_dict, contacts_list[0])

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(reuslt_list)