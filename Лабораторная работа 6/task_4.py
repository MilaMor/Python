import json

INPUT_FILE = "input.csv"
# создаем функцию - конвертер из csv  в json формат
def csv_to_list_dict(input_file, delimiter=',', new_line='\n') -> list[dict]:
    with open(input_file, 'r') as f:
        headers_ = f.readline().strip().split(delimiter)    # запись в список названия столбцов из файла
        _dict = [dict(zip(headers_, line.strip().split(delimiter))) for line in f.readlines()]
        # создали список словарей, с объединением двух значений: значения из названий столбцов и
        # значения ячеек сответствующих столбцов
    return _dict

print(json.dumps(csv_to_list_dict(INPUT_FILE),indent=4))
