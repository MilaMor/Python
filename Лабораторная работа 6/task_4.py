import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(input_file) -> list[dict]:
    dictionary_ = {}
    column_value = []
    list_value = []
    list_keys = []
    list_line = []
    list_final = []
    delimiter = ","
    new_line = "\n"
    with open(input_file) as f:
        for line in f:
            list_line.append(line.rsplit())     #добавить в список раздельные строки из исходных
    for line_l in list_line:
        if line_l == list_line[0]:      #есть ли строка в списке
            list_keys = line_l[0].split(delimiter)      #есть, разделитель,формирем список ключей
        else:
            column_value.append(line_l)      #отсутствует - > добавить в отдельный список
    for value in column_value:
        list_value.append(value[0].split(delimiter))      #добавить разделеные значения в список значений
    for l in range(len(list_line) - 1):
        list_line_l = list_value[l]       #делаем список порядковых номеров строк
        for key in range(len(list_keys)):
            dictionary_[list_keys[key]] = list_line_l[key]        #для каждого номера строки создаем словарь
        list_final.append(dictionary_.copy())      #вносим словари в итоговый список
    return list_final

print(json.dumps(csv_to_list_dict(INPUT_FILE),indent=4))
