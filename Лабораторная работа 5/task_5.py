import string
from random import sample
def get_random_password(count=8) -> str:
    list_password = sample([i for i in str(string.ascii_uppercase + string.ascii_lowercase + string.digits)], count)
    list_password = ''.join(str(d) for d in list_password)
    return list_password


print(get_random_password())
