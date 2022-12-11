from random import randint
start = -10
stop = 10
def get_unique_list_numbers(count=15) -> list[int]:
    list_num = []
    while len(list_num) < count:
        num = randint(start, stop)
        if num not in list_num:
            list_num.append(num)
    return list_num

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
